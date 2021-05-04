from app import db
from app.models.book import Book
from flask import request, Blueprint, Response, jsonify

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")


@books_bp.route("", methods=["GET", "POST"])
def books():
    if request.method == "GET":
        books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])

        db.session.add(new_book)
        db.session.commit()

        return Response(f"Book {new_book.title} successfully created", status=201)


@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def book(book_id):
    book = Book.query.get(book_id)

    if request.method == "GET":
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }
    # else
    elif request.method == "PUT":
        request_body = request.get_json()

        try:
            book.title = request_body["title"]
            book.description = request_body["description"]

            # Save Action
            # db.session.add(book)
            db.session.commit()
            return {
                    "id": book.id,
                    "title": book.title,
                    "description": book.description
            }, 200
        except KeyError:
            return {
                "message": "Request requires both 'title' and 'description'"
            }, 400
    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return {
            "Message": f"Book with title {book.title} has been deleted",
        }, 200