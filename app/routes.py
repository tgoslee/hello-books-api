from app import db
from app.models.book import Book
from flask import request, Blueprint, Response

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")


@books_bp.route("", methods=["POST"])
def books():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return Response(f"Book {new_book.title} successfully created", status=201)
