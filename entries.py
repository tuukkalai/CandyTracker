from flask import session, abort
from db import db
import users

def add_entry(candy, date, tokenc):
    if tokenc != session["tokenc"]:
        abort(403)
    try:
        user = users.user_id()
        sql = "INSERT INTO entries (user_id, candy_id, entry_time) VALUES (:user, :candy, :date)"
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

def get_additional_user_data():
    user = users.user_id()
    sql = "SELECT COUNT(e.id) AS count, ROUND(CAST(SUM(c.size) AS NUMERIC)/1000, 2) AS sum, ROUND(CAST(SUM(c.sugar) AS NUMERIC)/1000, 2) AS sugar FROM entries e INNER JOIN candies c ON e.candy_id=c.id WHERE e.user_id=:user"
    result = db.session.execute(sql,{"user":user})
    data = result.fetchone()
    return data