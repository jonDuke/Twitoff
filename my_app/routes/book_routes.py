# web_app/routes/book_routes.py

from my_app.models import db, Book, parse_records

from flask import Blueprint, jsonify, request, render_template, redirect

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    # return the books data in json format
    book_records = Book.query.all()
    return jsonify(book_records)

@book_routes.route("/books")
def list_books_for_humans():
    # list books
    book_records = Book.query.all()
    return render_template("books.html", message="Here are our books", 
                            books=book_records)

@book_routes.route("/books/new")
def new_book():
    # display the new book form
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["GET", "POST"])
def create_book():
    # add the new book to our dictionary
    new_book = Book(title=request.form["book_title"], 
                    author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()
    return redirect(f"/books")