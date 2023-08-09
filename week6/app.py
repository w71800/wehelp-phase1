from flask import Flask, render_template, request, redirect, url_for
from db_manufactor import db, cursor

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("home.html")

@app.route("/member")
def member():
  return render_template("member.html", name = None)

@app.route("/error")
def error():
  errorMsg = request.args.get("message")
  return render_template("error.html", message = errorMsg)

# 處理登入需求
@app.route("/signin", methods=["POST"])
def signin():
  user_id = request.form.get("user_id")
  user_password = request.form.get("user_password")
  # 先比對資料庫中有無此 id，有的話對對看密碼，沒有的話就要求申請帳號
  # 帳號密碼都對之後，重新導向至 /member，並且用 session 來存取 name
  return render_template("member.html")

# 處理註冊需求
@app.route("/signup", methods=["POST"])
def signup():
  user_username = request.form.get("id")
  sql = "SELECT username from member"
  cursor.execute(sql)
  signed_members = cursor.fetchall()
  signed_members = [ item[0] for item in signed_members ]
  
  # 已經被註冊的狀況
  if user_username in signed_members:
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


if __name__ == "__main__":
    app.run(port=3000, debug=True)

