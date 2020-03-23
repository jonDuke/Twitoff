# my_app/__init__.py

from flask import Flask, jsonify, render_template

from my_app.routes.home_routes import home_routes
from my_app.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    # @app.route("/")
    # def hello():
    #     print("VISITED THE HELLO PAGE")
    #     return "Hello World from __init__"

    # @app.route("/about")
    # def about():
    #     print("VISITED THE ABOUT PAGE")
    #     return "About Me!"

    # @app.route("/books")
    # def list_books():
    #     books = [
    #         {'id': 1, 'title': 'Book 1'},
    #         {'id': 2, 'title': 'Book 2'},
    #         {'id': 3, 'title': 'Book 3'}
    #     ]
    #     return render_template("books.html", books=books)

    # @app.route("/books.json")
    # def list_books_json():
    #     books = [
    #         {'id': 1, 'title': 'Book 1'},
    #         {'id': 2, 'title': 'Book 2'},
    #         {'id': 3, 'title': 'Book 3'}
    #     ]
    #     return jsonify(books)
    
    # @book_routes.route("/books/new")
    # def new_book():
    #     return render_template("new_book.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
