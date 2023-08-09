from flask import Flask, render_template, request, redirect, url_for, session
from db_manufactor import db, cursor, check_exist

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def home():
  return render_template("home.html")

@app.route("/member")
def member():
  is_signed = session.get("signed")

  if is_signed == False or is_signed == None:
    return redirect("/")
  
  name = session.get("name")
  return render_template("member.html", name = name)

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
    sql = "SELECT name, password FROM member WHERE username = %s"
    cursor.execute(sql, (user_id,))
    name, pwd = cursor.fetchall()[0]
    if pwd == user_password:
      session["name"] = name
      session["signed"] = True
      return redirect("/member")
    else:
      return redirect(url_for("error", message = "帳號或密碼輸入錯誤"))
  else:
    return redirect(url_for("error", message = "帳號或密碼輸入錯誤"))
  
  
  return "test"

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
  return redirect("/")

if __name__ == "__main__":
    app.run(port=3000, debug=True)

