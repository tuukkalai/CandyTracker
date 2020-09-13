import os
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from posix import abort

from db import db

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
            session["tokenc"] = os.urandom(16).encode('hex')
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["username"]
    del session["tokenc"]
    return True

def change_password(username, password, password2, oldPassword, tokenc):
    if tokenc != session["tokenc"]:
        abort(403)
    if password == password2:
        sql = "SELECT password FROM users WHERE username=:username"
        result = db.session.execute(sql,{"username":username})
        user = result.fetchone()
        if check_password_hash(user[0], oldPassword):
            sql = "UPDATE users SET password=:password WHERE username=:username"
            db.session.execute(sql,{"password":generate_password_hash(password),"username":username})
            db.session.commit()
            return [True, "Password updated"]
        else:
            return [False, "Incorrect old password"]
    else:
        return [False, "Passwords don't match"]