# my_app/routes/admin_routes.py

from flask import Blueprint, request, render_template, flash, redirect
from flask_basicauth import BasicAuth

from my_app.models import db, User, Tweet
from my_app.routes.twitter_routes import store_twitter_data

admin_routes = Blueprint("admin_routes", __name__)
basic_auth = BasicAuth()

# admin panel
@admin_routes.route("/admin")
@basic_auth.required
def admin_panel():
    users = User.query.all()
    return render_template("admin_panel.html", users=users)

# clears the entire database
@admin_routes.route("/admin/db/reset")
@basic_auth.required
def reset_db():
    db.drop_all()
    db.create_all()
    flash("Database cleared", "success")
    return redirect("/admin")

# seeds the database with a default set of users
@admin_routes.route("/admin/db/seed")
@basic_auth.required
def seed_db():
    default_users = ['elonmusk', 'austen', 's2t2', 'nbcnews', 'justinbieber']
    for user in default_users:
        store_twitter_data(user)

    flash("Default users added to database", "success")
    return redirect("/admin")

# removes a single user from the database
@admin_routes.route("/admin/db/remove/<screen_name>")
@basic_auth.required
def remove_user(screen_name=None):
    # see if the user exists
    try:
        user = User.query.filter_by(screen_name=screen_name).one()
    except:
        flash(f"User {screen_name} not found, cannot remove", "error")
        return redirect("/admin")

    # remove the user from the database
    Tweet.query.filter_by(user_id=user.id).delete()
    User.query.filter_by(screen_name=screen_name).delete()
    db.session.commit()

    flash(f"User {screen_name} removed from the database", "success")
    return redirect("/admin")

# re-adds all existing users to add any new tweets
@admin_routes.route("/admin/db/update/all")
@basic_auth.required
def update_all():
    # get existing users
    users = User.query.all()

    # informational, count tweets before and after
    before = 0
    after = 0

    # re-add all
    for user in users:
        before += user.tweet_count
        new_user, _ = store_twitter_data(user.screen_name)
        after += new_user.tweet_count

    flash(f"All users updated, added {after - before} new tweets", "success")
    return redirect("/admin")

# re-adds a single user to add any new tweets
@admin_routes.route("/admin/db/update/<screen_name>")
@basic_auth.required
def update_user(screen_name=None):
    # see if the user exists
    try:
        user = User.query.filter_by(screen_name=screen_name).one()
    except:
        flash(f"User {screen_name} not found, cannot update", "error")
        return redirect("/admin")
    
    # re-add the user
    before = user.tweet_count
    new_user, _ = store_twitter_data(user.screen_name)
    after = new_user.tweet_count
    
    flash(f"User {screen_name} updated, added {after - before} new tweets", "success")
    return redirect("/admin")
