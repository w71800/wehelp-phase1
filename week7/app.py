from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from db_manufactor import db, cursor, check_exist
from data_validator import formatIsOk, hasSpace

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.secret_key = "secret"


@app.route("/")
def home():
  return render_template("home.html")

@app.route("/member")
def member():
  is_signed = session.get("signed")

  if is_signed in [ None, False ]:
    return redirect("/")
  
  username = session.get("name")
  # 抓取留言資料
  sql = "SELECT message.id, name, content from message LEFT JOIN member ON message.member_id = member.id"
  cursor.execute(sql)
  result = cursor.fetchall()
  msgs = []
  
  for item in result:
    id, name, content = item
    dict = { "id": id, "name": name, "content": content }
    msgs.append(dict)

  return render_template("member.html", name = username, msgs = msgs)

@app.route("/error")
def error():
  errorMsg = request.args.get("message")
  
  return render_template("error.html", message = errorMsg)

# 處理登入需求
@app.route("/signin", methods=["POST"])
def signin():
  user_id = request.form.get("user_id")
  user_password = request.form.get("user_password")
  # 先比對資料庫中有無此 id，有的話對對看密碼
  is_exist = check_exist(user_id)
  
  if is_exist:
    sql = "SELECT name, password, id FROM member WHERE username = %s"
    cursor.execute(sql, (user_id,))
    name, pwd, member_id = cursor.fetchall()[0]
    if pwd == user_password:
      session["name"] = name
      session["signed"] = True
      session["member_id"] = member_id
      return redirect("/member")
    else:
      return redirect(url_for("error", message = "帳號或密碼輸入錯誤"))
  else:
    return redirect(url_for("error", message = "帳號或密碼輸入錯誤"))

# 處理註冊需求
@app.route("/signup", methods=["POST"])
def signup():
  user_username = request.form.get("id")
  is_exist = check_exist(user_username)
  
  # 已經被註冊的狀況
  if is_exist:
    return redirect(url_for("error", message = "帳號已經被註冊"))
  # 新用戶的狀況
  else:
    user_name = request.form.get("name")
    user_password = request.form.get("password")
    sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    values = (user_name, user_username, user_password)
    cursor.execute(sql, values)
    db.commit()

    return redirect("/")

@app.route("/signout")
def signout():
  session.pop("name", None)
  session.pop("signed", None)
  session.pop("member_id", None)
  
  return redirect("/")

@app.route("/createMessage", methods=["POST"])
def create_message():
  content = request.form.get("content")
  
  # 需要：member_id, content
  sql = "INSERT into message(member_id, content) value(%s, %s)"
  value = (session.get("member_id"), content)
  cursor.execute(sql, value)
  db.commit()

  return redirect("/member")

@app.route("/deleteMessage", methods=["POST"])
def delete_message():
  delID = int(request.data.decode("utf-8"))
  
  sql = "DELETE from message where id = %s"
  cursor.execute(sql, (delID,))
  db.commit()

  return "OK"

@app.route("/api/member/<id>")
def restful_api_member(id):
  method = request.method
  response = None
  if session.get("signed") in [False, None]:
    response = jsonify({ "data": None }) if method == "GET" else jsonify({ "error": True })
    return response
  else:
    # 以 restful API 形式透過 id 存取
    if id is not None:
      sql = "SELECT id, name, username from member where id = (%s);"
      cursor.execute(sql, (id, ))
      result = cursor.fetchall()
    
    if len(result) == 0:
      response = jsonify({ "id": None, "name": None, "username": None })
    else:
      id, name, username = result[0]
      response = jsonify({ "id": id, "name": name, "username": username })
    
    return response

# 處理靜態路由
@app.route("/api/member", methods = ["GET", "PATCH"])
def api_member():
  method = request.method
  if session.get("signed") in [False, None]:
    response = jsonify({ "data": None }) if method == "GET" else jsonify({ "error": True })

    return response

  else:
    if method == "PATCH":
      new_name = request.json["name"]
      member_id = session["member_id"]
      
      ### 錯誤格式驗證：如果是空的話 ###
      if hasSpace(new_name):
        response = jsonify({ "error": True, "message": "The format of input is unvalid"})

        return response
      ##############################
      sql = "UPDATE member SET name = (%s) where id = (%s)"
      cursor.execute(sql, (new_name, member_id))
      db.commit()
    
      session["name"] = new_name
      response = jsonify({ "ok": True })

      return response
    
    if method == "GET":
      query = request.args.get("username")
      if query is not None:
        ### 錯誤格式驗證：如果是整坨有空白的話 ###
        if hasSpace(query):
          response = jsonify({ "error": True, "message": "The format of input is unvalid" })

          return response
        ##############################
        sql = "SELECT id, name, username from member where username = (%s);"
        cursor.execute(sql, (query, ))
        result = cursor.fetchall()
            
        if len(result) == 0:
          response = jsonify({ "id": None, "name": None, "username": None })
        else:
          id, name, username = result[0]
          response = jsonify({ "id": id, "name": name, "username": username })
      else:
        response = jsonify({ "error": True, "message": "There's no query string" })
  
      return response



if __name__ == "__main__":
    app.run(port=3000, debug=True)

