from app import app
from flask import flash, redirect, render_template, request, session, abort, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

from db import db
import users
import entries
import candies
import groups
import json

# Root
@app.route("/")
def home():
    return render_template("home.html")

# Error handlers
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", error=error), 404

@app.errorhandler(403)
def user_not_authorized(error):
    return render_template("404.html", error=error), 403

@app.errorhandler(500)
def internal_error(error):
    return render_template("404.html"), 500

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("home.html", notification="User not found or incorrect password")

# User's pages
@app.route("/logout")
def logout():
    if users.logout():
        return redirect("/")
    return render_template("home.html", notification="Something went wrong.")

@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "GET":
        return render_template("settings.html")
    if request.method == "POST":
        password = request.form["new-pass1"]
        password2 = request.form["new-pass2"]
        oldPassword = request.form["prev-pass"]
        tokenc = request.form["tokenc"]
        change = users.change_password(password, password2, oldPassword, tokenc)
    return render_template("settings.html", notification=change[1])

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("new_user.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        passwordAgain = request.form["password_again"]
        if users.create_user(username, password, passwordAgain):
            return redirect("/")
        else:
            return render_template("new_user.html", username=username, notification="Username already taken, or password mismatch")

# Diary
@app.route("/diary", methods=["GET", "POST"])
def diary():
    if not users.authenticated():
        abort(403)
    if request.method == "GET":
        all_candies = candies.get_all_candies()
        daily_entries = entries.get_sum_of_days()
        user_data = entries.get_additional_user_data()
        all_entries = entries.get_all_entries()
        return render_template("diary.html", candies=all_candies, daily_entries=daily_entries, user_data=user_data, all_entries=all_entries)
    if request.method == "POST":
        candy = request.form["select-candy"]
        date = request.form["candy-date"]
        tokenc = request.form["tokenc"]
        new_name = request.form["add-candy-name"]
        new_company = request.form["add-candy-company"]
        new_weight = request.form["add-candy-weight"]
        new_sugar = request.form["add-candy-sugar"]
        new_gtin = request.form["add-candy-gtin"]
        new_category = request.form["add-candy-category"]
        if new_name != '':
            candy = candies.add_candy(new_name, new_company, new_weight, new_sugar, new_gtin, new_category)
        if entries.add_entry(candy, date, tokenc):
            return redirect("/diary")

@app.route("/entries/<int:id>/delete", methods=["GET"])
def delete_entry(id):
    if not users.authenticated():
        abort(403)
    if entries.delete_entry(id):
        return redirect("/diary")

# Groups
@app.route("/groups", methods=["GET", "POST"])
def get_groups_post_group():
    if not users.authenticated():
        abort(403)
    else:
        users_groups = groups.get_user_groups()
        public_groups = groups.get_public_groups()
        create = False if len(users_groups) > 5 else True
    if request.method == "GET":
        return render_template("groups.html", groups=users_groups, create=create, public_groups=public_groups)
    if request.method == "POST":
        group_name = request.form["group-name"]
        tokenc = request.form["tokenc"]
        group = groups.create_group(group_name, tokenc)
        if group > 0:
            return redirect("/groups/"+str(group))
        else:
            return render_template("groups.html", 
                    notification="Group not created, something went wrong", 
                    groups=users_groups, 
                    create=create, 
                    public_groups=public_groups)

@app.route("/groups/<int:group_id>", methods=["GET"])
def get_single_group(group_id):
    group_info = groups.get_group_details(group_id)
    if not group_info:
        return render_template("group.html", notification="No access to this group", group_info="No access")
    else:
        is_group_admin = users.is_group_admin(group_id)
        messages = groups.get_messages(group_id)
        return render_template("group.html", group_id=group_id, group_info=group_info, group_admin=is_group_admin, messages=messages)
        
@app.route("/groups/<int:group_id>/<string:action>/<string:username>", methods=["GET"])
def allow_reject_user_group(action, group_id, username):
    if action == "accept" and groups.accept_user_to_group(group_id, username):
        return redirect("/groups/"+str(group_id))
    if action == "reject" and groups.reject_user_from_group(group_id, username):
        return redirect("/groups/"+str(group_id))
    if action == "remove" and groups.remove_member_from_group(group_id, username):
        if username == users.username():
            return redirect("/groups")
        return redirect("/groups/"+str(group_id))

@app.route("/groups/<int:group_id>/request", methods=['GET'])
def request_to_group(group_id):
    if not users.authenticated():
        abort(403)
    if groups.user_request_to_group(group_id):
        flash("Request sent to group")
    else:
        flash("Previous request waiting for groups approval")
    return redirect("/groups")

@app.route("/groups/<int:group_id>/public", methods=["GET"])
def toggle_group_public_private(group_id):
    if groups.toggle_public_private(group_id):
        flash("Group publicness changed")
    return get_single_group(group_id)

@app.route("/groups/<int:group_id>/send", methods=["POST"])
def send_message(group_id):
    content = request.form["msg"]
    if groups.send_message(group_id, content):
        return redirect("/groups/"+str(group_id))