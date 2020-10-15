import os
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from posix import abort

from db import db

def authenticated():
    if user_id() > 0:
        return True
    return False

def is_admin():
    sql = "SELECT auth FROM users WHERE id=:user"
    result = db.session.execute(sql,{"user":user_id()})
    user_auth = result.fetchone()[0]
    if user_auth == 'admin':
        return True
    return False

def is_group_admin(group_id):
    sql = "SELECT members[1] FROM groups WHERE id=:group_id"
    result = db.session.execute(sql, {"group_id":group_id})
    admin = result.fetchone()[0]
    if user_id() == admin:
        return True
    return False

def user_id():
    return session.get("user_id",0)

def username():
    return session.get("username",0)

def login(username, password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql,{"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            # If user credentials are correct add items to session
            session["user_id"] = user[1]
            session["username"] = username
            session["tokenc"] = os.urandom(16).encode('hex') # local
            # session["tokenc"] = os.urandom(16).hex()       # prod
            return True
        else:
            return False

def logout():
    # Remove added items from session
    del session["user_id"]
    del session["tokenc"]
    del session["username"]
    return True

def change_password(password, password2, oldPassword, tokenc):
    # Allow user with correct session token to update password
    # Return tuple with first value (boolean) based on success
    # and second as a notification text
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
    # Check if username is available and two password inputs match
    # Return to login with new credentials or back to create user page
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    unamesInDb = result.fetchone()
    if unamesInDb != None:
        return False
    if password == passwordAgain:
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
        return login(username, password)
    return False
