# my_app/routes/admin_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from my_app.models import db
from my_app.routes.twitter_routes import store_twitter_data

admin_routes = Blueprint("admin_routes", __name__)

@admin_routes.route("/admin/db/reset")
def reset_db():
    print(type(db))
    db.drop_all()
    db.create_all()
    return jsonify({"message": "DB RESET OK"})

@admin_routes.route("/admin/db/seed")
def seed_db():
    print(type(db))
    # TODO: refactor the existing user and tweet storage logic from our twitter_routes into a re-usable function
    # ... so we can "seed" our database with some example users and tweets
    # ... to ensure that it is ready to make predictions later

    default_users = ['elonmusk', 'austen', 's2t2', 'nbcnews', 'justinbieber']
    for user in default_users:
        store_twitter_data(user)

    return jsonify({"message": f"DB SEEDED OK (with {len(default_users)} users)"})
