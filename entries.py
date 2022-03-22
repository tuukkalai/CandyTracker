from flask import session, abort
from db import db
import users

def add_entry(candy, date, tokenc):
    if tokenc != session["tokenc"]:
        abort(403)
    try:
        user = users.user_id()
        sql = """INSERT INTO entries (user_id, candy_id, entry_time)
                VALUES (:user, :candy, :date)"""
        db.session.execute(sql,{"user":user,"candy":candy,"date":date})
        db.session.commit()
        return True
    except:
        return False

def delete_entry(id):
    try:
        user = users.user_id()
        sql = "UPDATE entries SET visible=false WHERE user_id=:user AND id=:id"
        db.session.execute(sql,{"user":user,"id":id})
        db.session.commit()
        return True
    except:
        return False

def get_sum_of_days():
    user = users.user_id()
    sql = """SELECT SUM(c.size) AS total, e.entry_time 
            FROM entries e 
            INNER JOIN candies c 
            ON e.candy_id = c.id 
            WHERE e.user_id = :user 
            AND e.entry_time >= NOW()-INTERVAL '92 DAYS' 
            AND e.visible=true 
            GROUP BY e.entry_time"""
    result = db.session.execute(sql,{"user":user})
    sums = result.fetchall()
    return sums

def get_additional_user_data():
    user = users.user_id()
    # Get count, sum, sugar and diff from database with single query
    # Values showed in Diary > Your additional stats
    sql = """SELECT COUNT(e.id) AS count, 
            ROUND(CAST(SUM(c.size) AS NUMERIC)/1000, 2) AS sum, 
            ROUND(CAST(SUM(c.sugar) AS NUMERIC)/1000, 2) AS sugar, 
            (
                SELECT SUM(c.size) 
                FROM candies c 
                INNER JOIN entries e 
                ON e.candy_id=c.id 
                WHERE e.user_id=:user 
                AND e.entry_time > CURRENT_DATE-7 
                AND e.visible=true
            )-(
                SELECT SUM(c.size) 
                FROM candies c 
                INNER JOIN entries e 
                ON e.candy_id=c.id 
                WHERE e.user_id=:user 
                AND e.entry_time <= CURRENT_DATE-7 
                AND e.entry_time > CURRENT_DATE-14 
                AND e.visible=true
            ) AS diff 
            FROM entries e 
            INNER JOIN candies c 
            ON e.candy_id=c.id 
            WHERE e.user_id=:user 
            AND e.visible=true"""
    result = db.session.execute(sql,{"user": user})
    data = result.fetchone()
    return data

def get_all_entries():
    user = users.user_id()
    sql = """SELECT 
                e.id,
                c.name,
                TO_CHAR(e.entry_time :: DATE, 'dd.mm.yyyy') AS entry_time
            FROM entries e 
            INNER JOIN candies c 
            ON e.candy_id=c.id 
            WHERE e.user_id=:user 
            AND e.visible=true 
            ORDER BY entry_time DESC"""
    result = db.session.execute(sql,{"user": user})
    data = result.fetchall()
    return data