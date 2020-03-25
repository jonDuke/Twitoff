# my_app/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    return render_template("twitoff_selection.html")

@home_routes.route("/hello")
def hello():
    return render_template("index.html")

@home_routes.route("/about")
def about():
    return "About me"