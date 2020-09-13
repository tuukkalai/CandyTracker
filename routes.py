from app import app
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash

from db import db
import users
import entries
import json

@app.route("/")
def home():
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template("404.html"), 500

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
        return redirect("/")
    else:
        return render_template("home.html", notification="User not found or incorrect password")

@app.route("/logout")
def logout():
    if users.logout():
        return redirect("/")
    return render_template("home.html", notification="Something went wrong.")

@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "GET":
        return render_template("settings.html")
    if request.method == "POST":
        password = request.form["newPass1"]
        password2 = request.form["newPass2"]
        oldPassword = request.form["prevPass"]
        tokenc = request.form["tokenc"]
        change = users.change_password(password, password2, oldPassword, tokenc)
    return render_template("settings.html", notification=change[1])

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("new_user.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        passwordAgain = request.form["password_again"]
        create = users.create_user(username, password, passwordAgain)
        if create[0]:
            return redirect("/")
        else:
            return render_template("new_user.html", username=username, notification=create[1])

@app.route("/diary", methods=["GET", "POST"])
def diary():
    if request.method == "GET":
        sql = "SELECT id, name, company FROM candies"
        result = db.session.execute(sql)
        candies = result.fetchall()
        return render_template("diary.html", candies=candies)
    if request.method == "POST":
        candy = request.form["candy-search"]
        date = request.form["candy-date"]
        tokenc = request.form["tokenc"]
        if entries.add_entry(candy, date, tokenc):
            return redirect("/diary")


"""
Training material
---
"""
# Pizza
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

# Messages
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

# Polls
@app.route("/polls")
def poll():
    sql = "SELECT id, topic FROM polls"
    result = db.session.execute(sql)
    polls = result.fetchall()
    return render_template("polls.html", polls=polls)

@app.route("/polls/<int:id>")
def showPoll(id):
    sql = "SELECT topic, created_at FROM polls WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    res = result.fetchone()
    if res:
        topic = res[0]
        created = res[1].strftime("%d.%m.%Y %H.%M")
        sql = "SELECT id, choice FROM choices WHERE poll_id=:id"
        result = db.session.execute(sql, {"id":id})
        choices = result.fetchall()
        return render_template("poll.html", topic=topic, choices=choices, created=created, id=id)
    return 

@app.route("/polls/answer", methods=["POST"])
def ans():
    choice_id = request.form["choice"]
    poll_id = request.form["id"]
    sql = "INSERT INTO answers (choice_id, sent_at) VALUES (:choice_id, NOW())"
    db.session.execute(sql, {"choice_id":choice_id})
    db.session.commit()
    return redirect("/results/"+str(poll_id))

@app.route("/results/<int:id>")
def showResults(id):
    sql = "SELECT topic FROM polls WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    topic = result.fetchone()[0]
    sql = "SELECT c.choice, COUNT(a.id) FROM choices c LEFT JOIN answers a ON c.id = a.choice_id WHERE c.poll_id=:poll_id GROUP BY c.id"
    result = db.session.execute(sql, {"poll_id":id})
    choices = result.fetchall()
    total = 0
    for c in choices:
        total += c[1]
    return render_template("results.html", topic=topic, choices=choices, total=total)

@app.route("/polls/new")
def newPollForm():
    return render_template("new_poll.html")

@app.route("/polls/create", methods=["POST"])
def createPoll():
    topic = request.form["topic"]
    sql = "INSERT INTO polls (topic, created_at) VALUES (:topic, NOW()) RETURNING id"
    result = db.session.execute(sql, {"topic":topic})
    poll_id = result.fetchone()[0]
    choices = request.form.getlist("choice")
    values = ""
    for choice in choices:
        if choice != "":
            values += "("+str(poll_id)+", '"+choice+"'), "
    sql = "INSERT INTO choices (poll_id, choice) VALUES "+values[:-2]
    db.session.execute(sql)
    db.session.commit()
    return redirect("/polls")

"""
Training ends
---
"""