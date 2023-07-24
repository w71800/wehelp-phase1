from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/signin", methods=["POST"]) 
def signIn():
  return "來到登入頁面了"



if __name__ == "__main__":
  app.run(debug=True)