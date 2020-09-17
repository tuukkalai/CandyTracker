from flask import session
from posix import abort

from db import db

def get_candies():
    sql = "SELECT name FROM candies"
    result = db.session.execute(sql)
    candies = result.fetchall()
    return candies

def add_candy(name, company, weight, sugar, gtin, category):
    sql = "INSERT INTO candies (name, company, size, sugar, gtin, category) VALUES (:name, :company, :size, :sugar, :gtin, :category) RETURNING id"
    result = db.session.execute(sql,{"name":name, "company":company, "size":int(weight), "sugar":int(sugar), "gtin":int(gtin), "category":category})
    candy_id = result.fetchone()[0]
    return candy_id

