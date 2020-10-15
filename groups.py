from flask import session, abort
from db import db
import users

def get_user_groups():
    user = users.user_id()
    sql = """SELECT id, name 
            FROM groups 
            WHERE members @> ARRAY[:user] 
            AND visible=true"""
    result = db.session.execute(sql, {"user":user})
    data = result.fetchall()
    return data

def get_public_groups():
    user = users.user_id()
    sql = """SELECT id, name 
        FROM groups 
        WHERE open=true
        AND NOT(members @> ARRAY[:user])
        AND visible=true"""
    result = db.session.execute(sql, {"user":user})
    data = result.fetchall()
    return data

def create_group(group_name, tokenc):
    if tokenc != session["tokenc"]:
        abort(403)

    # Add new group to database and current user as a member to that group
    user = users.user_id()
    sql = "INSERT INTO groups (name, members) VALUES (:group, ARRAY[:user])"
    db.session.execute(sql,{"group":group_name, "user":user})
    db.session.commit()

    # RETURNING doesn't seem to work when adding values in array
    # id of the new group is fetched with additional query
    sql = "SELECT id FROM groups WHERE name=:group"
    result = db.session.execute(sql,{"group":group_name})
    group_id = result.fetchone()[0]
    return group_id

def get_group_details(group_id):
    if users.is_admin() or (users.authenticated and group_id in [n.id for n in get_user_groups()]):
        # Select single row on information combining name of the group, number of users in the group and
        # usernames of all the requests for joining the group
        sql = """SELECT name, 
                array_length(members,1) AS no_of_members,
                (
                    SELECT ARRAY(
                        SELECT username 
                        FROM users 
                        WHERE id IN (
                            SELECT UNNEST(requests) 
                            FROM groups 
                            WHERE id=:group_id
                        )
                    )
                ) AS requests
                FROM groups 
                WHERE id=:group_id"""
        result = db.session.execute(sql,{"group_id":group_id})
        group_info = result.fetchall()[0]
        return group_info
    else:
        return False
    
# Fetch usernames of members
# sql = """SELECT username 
#         FROM users 
#         WHERE id IN (
#             SELECT unnest(members) 
#             FROM groups 
#             WHERE id=:group_id
#         )"""
# result = db.session.execute(sql,{"group":group_id})
# users_in_group = result.fetchall()


def accept_user_to_group(group_id, username):
    if users.is_admin() or (users.authenticated and group_id in [n.id for n in get_user_groups()]):
        try:
            # Add user with username to members and remove user from group requests
            sql = """UPDATE groups 
                    SET members=members || (SELECT id FROM users WHERE username=:username),
                        requests=array_remove(requests,(SELECT id FROM users WHERE username=:username))
                    WHERE id=:group_id"""
            db.session.execute(sql, {"username":username, "group_id":group_id})
            db.session.commit()
            return True
        except:
            return False

def user_request_to_group(group_id):
    user = users.user_id()
    sql = "SELECT 1 FROM groups WHERE requests @> ARRAY[:user] AND id=:group_id"
    result = db.session.execute(sql,{"user":user, "group_id":group_id})
    if result.fetchone() != None:
        print('Request already in place')
        return False
    print('No prior requests')
    sql = "UPDATE groups SET requests=requests || :user WHERE id=:group_id"
    db.session.execute(sql,{"user":user, "group_id":group_id})
    db.session.commit()
    return True

def remove_member_from_group(user_id, group_id):
		# If user is groups admin (first member), user is able to remove other users from group
		if users.is_group_admin(group_id) or users.is_admin():
    		sql = "UPDATE groups SET members=array_remove(members,:user_id) WHERE id=:group_id"
				db.session.execute(sql, {"user_id":user_id,"group_id":group_id})
				db.session.commit()
				return True
		return False
