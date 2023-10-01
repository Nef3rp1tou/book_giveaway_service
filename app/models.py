from app import db

class Book(db.Model):
    id = db.Column(db.String(13), primary_key=True)  # ISBN is used as the primary key
    title = db.Column(db.String(256))
    author = db.Column(db.String(128))
    cover_url = db.Column(db.String(256))  # URL to the book cover image
