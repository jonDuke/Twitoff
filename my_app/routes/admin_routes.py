# my_app/routes/admin_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from my_app.models import db, User
from my_app.routes.twitter_routes import store_twitter_data

admin_routes = Blueprint("admin_routes", __name__)

@admin_routes.route("/admin")
def admin_panel():
    users = User.query.all()
    return render_template("admin_panel.html", users=users)

@admin_routes.route("/admin/db/reset")
def reset_db():
    db.drop_all()
    db.create_all()
    return jsonify({"message": "DB RESET OK"})

@admin_routes.route("/admin/db/seed")
def seed_db():
    default_users = ['elonmusk', 'austen', 's2t2', 'nbcnews', 'justinbieber']
    for user in default_users:
        store_twitter_data(user)

    return jsonify({"message": f"DB SEEDED OK (with {len(default_users)} users)"})
