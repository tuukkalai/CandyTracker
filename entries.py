from flask import session, abort
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

def get_sum_of_days():
    user = users.user_id()
    sql = "SELECT SUM(c.size) AS total, e.entry_time FROM entries e INNER JOIN candies c ON e.candy_id = c.id WHERE e.user_id = :user AND e.entry_time >= NOW()-INTERVAL '92 DAYS' GROUP BY e.entry_time"
    result = db.session.execute(sql,{"user":user})
    sums = result.fetchall()
    return sums