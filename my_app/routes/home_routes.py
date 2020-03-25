# my_app/routes/home_routes.py

from flask import Blueprint, render_template

from my_app.models import User

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    # get list of users for the drop-down menus
    userlist = User.query.all()
    return render_template("twitoff_selection.html", userlist=userlist)

@home_routes.route("/hello")
def hello():
    return render_template("index.html")

@home_routes.route("/about")
def about():
    return "About me"