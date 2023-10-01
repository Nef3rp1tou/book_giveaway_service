from flask import Blueprint, jsonify
from app import db
from app.models import Book
import requests

bp = Blueprint('books', __name__, url_prefix='/books')


@bp.route('/fetch', methods=['POST'])
def fetch_books():
    # Define a list of ISBNs you want to fetch from the Open Library API
    isbns_to_fetch = ["9780451524935", "9780141983769"]  # Add more ISBNs as needed

    for isbn in isbns_to_fetch:
        book_data = fetch_book_data(isbn)
        if book_data:
            store_book_data(book_data)

    return jsonify({"message": "Books fetched and stored successfully"})


def fetch_book_data(isbn):
    try:
        response = requests.get(f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json")
        if response.status_code == 200:
            book_data = response.json().get(f"ISBN:{isbn}", {})
            return {
                "id": isbn,
                "title": book_data.get("title", ""),
                "author": ", ".join(book_data.get("authors", [{}])[0].get("name", "")),
                "cover_url": book_data.get("cover", {}).get("medium", "")
            }
    except Exception as e:
        print(f"Error fetching book data for ISBN {isbn}: {str(e)}")
    return None


def store_book_data(book_data):
    book = Book.query.get(book_data["id"])
    if not book:
        book = Book(
            id=book_data["id"],
            title=book_data["title"],
            author=book_data["author"],
            cover_url=book_data["cover_url"]
        )
        db.session.add(book)
        db.session.commit()

@bp.route('/get/<isbn>', methods=['GET'])
def get_book(isbn):
    book = Book.query.get(isbn)
    if book:
        return jsonify({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "cover_url": book.cover_url
        })
    else:
        return jsonify({"message": "Book not found"}), 404
