from flask import session, abort
from db import db
import users

def get_user_groups():
    user = users.user_id()
    sql = "SELECT id, name FROM groups WHERE members @> ARRAY[:user] AND visible = true"
    result = db.session.execute(sql, {"user":user})
    data = result.fetchall()
    return data

def create_group(group, tokenc):
    if tokenc != session["tokenc"]:
        abort(403)

    # Add new group to database and current user as a member to that group
    user = users.user_id()
    sql = "INSERT INTO groups (name, members) VALUES (:group, ARRAY[:user])"
    db.session.execute(sql,{"group":group, "user":user})
    db.session.commit()

    # RETURNING doesn't seem to work when adding values in array
    # id of the new group is fetched with additional query
    sql = "SELECT id FROM groups WHERE name=:group"
    result = db.session.execute(sql,{"group":group})
    group_id = result.fetchone()[0]
    return group_id

def add_member_to_group(member_id, group):
    sql = "UPDATE groups SET members=members || :member_id where name=:group"

def remove_member_from_group(member_id, group):
    sql = "UPDATE groups SET members=array_remove(members,:member_id) WHERE name=:group"