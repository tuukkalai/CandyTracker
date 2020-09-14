import os
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from posix import abort

from db import db

def authenticated():
    if user_id() > 0:
        return True
    return False

def user_id():
    return session.get("user_id",0)

def login(username, password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql,{"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            session["username"] = username
            session["tokenc"] = os.urandom(16).hex() # os.urandom(16).encode('hex')
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["tokenc"]
    del session["username"]
    return True

def change_password(password, password2, oldPassword, tokenc):
    if tokenc != session["tokenc"]:
        abort(403)
    if password == password2:
        userid = user_id()
        sql = "SELECT password FROM users WHERE id=:userid"
        result = db.session.execute(sql,{"userid":userid})
        user = result.fetchone()
        if check_password_hash(user[0], oldPassword):
            sql = "UPDATE users SET password=:password WHERE id=:userid"
            db.session.execute(sql,{"password":generate_password_hash(password),"userid":userid})
            db.session.commit()
            return [True, "Password updated"]
        else:
            return [False, "Incorrect old password"]
    else:
        return [False, "Passwords don't match"]

def create_user(username, password, passwordAgain):
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    numOfUnames = result.fetchone()
    if numOfUnames > 0:
        return [False, "Username already taken."]
    if password == passwordAgain:
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
        return login(username, password)
    return [False, "Passwords don't match."]
