# my_app/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask

from my_app.models import db, migrate
from my_app.routes.home_routes import home_routes
from my_app.routes.book_routes import book_routes
from my_app.routes.twitter_routes import twitter_routes
from my_app.routes.admin_routes import admin_routes
from my_app.routes.iris_routes import iris_routes
from my_app.routes.stats_routes import stats_routes

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "super secret" # todo: pass from env var (enables flash messaging)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_app_12.db"
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/thedo/lambda_u3/sprint-3/my-web-app/my_app_12.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # set up authentication variables for admin controls
    load_dotenv()
    app.config['BASIC_AUTH_USERNAME'] = os.getenv("ADMIN_NAME")
    app.config['BASIC_AUTH_PASSWORD'] = os.getenv("ADMIN_PASS")
    app.config['BASIC_AUTH_REALM'] = 'admin'

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(iris_routes)
    app.register_blueprint(stats_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
