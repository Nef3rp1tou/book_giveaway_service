from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Create Flask app instance
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import your routes and blueprints here
from app.routes import auth, books, other_resources

# Register blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(books.bp)
app.register_blueprint(other_resources.bp)
from app.routes import books

# ...
# Register the books blueprint
app.register_blueprint(books.bp)
