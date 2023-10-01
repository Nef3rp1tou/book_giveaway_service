from flask import Blueprint

# Create a blueprint for each route module
auth = Blueprint('auth', __name__, url_prefix='/auth')
books = Blueprint('books', __name__, url_prefix='/books')
other_resources = Blueprint('other_resources', __name__, url_prefix='/other')

# Import your route modules here
from app.routes import auth, books, other_resources
