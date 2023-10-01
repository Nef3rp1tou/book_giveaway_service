import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.getcwd(), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Add more configuration options as needed