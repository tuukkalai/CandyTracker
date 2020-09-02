from os import getenv
from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    words = ["apina","banaani","cembalo"]
    return render_template("index.html",message="Tervetuloa!",items=words)

@app.route("/order")
def form():
    return render_template("order.html")

@app.route("/result", methods=["POST"])
def result():
    pizza = request.form["pizza"]
    extras = request.form.getlist("extra")
    msg = request.form["message"]
    return render_template("result.html", 
        pizza=pizza, 
        extras=extras, 
        message=msg)

@app.route("/messages")
def messages():
    result = db.session.execute("SELECT COUNT(*) FROM messages")
    count = result.fetchone()[0]
    result = db.session.execute("SELECT content FROM messages")
    messages = result.fetchall()
    return render_template("messages.html", count=count, messages=messages)

@app.route("/messages/new")
def new():
    return render_template("new.html")

@app.route("/messages/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = "INSERT INTO messages (content) VALUES (:content)"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/messages")