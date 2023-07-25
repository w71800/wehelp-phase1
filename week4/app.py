from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/signin", methods=["POST"]) 
def signIn():
  userId = request.form.get("id")
  userpwd = request.form.get("password")

  print(userId, userpwd)
  if userId and userpwd == "test":
    session["SIGNED-IN"] = True
    return redirect("/member")
  elif userId == "" or userpwd == "" :
    errorMsg = "Please enter username and password"
    return redirect(url_for("error", message = errorMsg))
  else:
    errorMsg = "Username or password is not correct"
    return redirect(url_for("error", message = errorMsg))

@app.route("/member") 
def member():
  SIGNED_IN = session.get("SIGNED-IN")

  print(SIGNED_IN)
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




if __name__ == "__main__":
  app.run(port=3000, debug=True)