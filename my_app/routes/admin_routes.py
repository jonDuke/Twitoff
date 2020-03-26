# my_app/routes/admin_routes.py

from flask import Blueprint, request, render_template, flash, redirect
from flask_basicauth import BasicAuth

from my_app.models import db, User
from my_app.routes.twitter_routes import store_twitter_data

admin_routes = Blueprint("admin_routes", __name__)
basic_auth = BasicAuth()

@admin_routes.route("/admin")
@basic_auth.required
def admin_panel():
    users = User.query.all()
    return render_template("admin_panel.html", users=users)

@admin_routes.route("/admin/db/reset")
@basic_auth.required
def reset_db():
    db.drop_all()
    db.create_all()
    flash("Database cleared", "success")
    return redirect("/admin")

@admin_routes.route("/admin/db/seed")
@basic_auth.required
def seed_db():
    default_users = ['elonmusk', 'austen', 's2t2', 'nbcnews', 'justinbieber']
    for user in default_users:
        store_twitter_data(user)

    flash("Default users added to database", "success")
    return redirect("/admin")
