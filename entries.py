from flask import session
from db import db
import users

def add_entry(candy, date, tokenc):
    if tokenc != session["tokenc"]:
        abort(403)
    try:
        user = users.user_id()
        sql = "INSERT INTO entries (user_id, candy_id, entry_time) VALUES (:user, (SELECT id FROM candies WHERE name=:candy), :date)"
        db.session.execute(sql,{"user":user,"candy":candy,"date":date})
        db.session.commit()
        return True
    except:
        return False