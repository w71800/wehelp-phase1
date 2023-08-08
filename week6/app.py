from flask import Flask, render_template, request, redirect
from db_manufactor import cursor

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
  # 帳號密碼都對之後，帶著 name 重新導向至 /member
  return render_template("member.html")

if __name__ == "__main__":
    app.run(port=3000, debug=True)

