from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret"

app.static_folder = "static"

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/signin", methods=["POST"]) 
def signIn():
  userId = request.form.get("id")
  userpwd = request.form.get("password")

  if userId == "test" and userpwd == "test":
    session["SIGNED-IN"] = True
    return redirect("/member")
  elif userId == "" or userpwd == "" :
    errorMsg = "帳號或密碼有缺，請補上"
    return redirect(url_for("error", message = errorMsg))
  else:
    errorMsg = "帳號或密碼有誤，請更正"
    return redirect(url_for("error", message = errorMsg))

@app.route("/member") 
def member():
  SIGNED_IN = session.get("SIGNED-IN")
  if SIGNED_IN:
    return render_template("member.html")
  else:
    return redirect("/")

@app.route("/signout") 
def signout():
  SIGNED_IN = session.get("SIGNED-IN")
  if SIGNED_IN:
    session.pop("SIGNED-IN")
    return redirect("/")

@app.route("/error") 
def error():
  errorMsg = request.args.get("message")
  return render_template("error.html", message = errorMsg)

@app.route("/square/", methods=["POST"]) 
def square_post():
  return "你好"

@app.route("/square/<squared_num>") 
def square(squared_num):
  print(squared_num)
  return render_template("result.html", result = squared_num)




if __name__ == "__main__":
  app.run(port=3000, debug=True)