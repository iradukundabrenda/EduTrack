# app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Create a database instance (this will connect to your app later)
db = SQLAlchemy()

# User model represents each user in your app
class User(db.Model, UserMixin):
    __tablename__ = 'users'  # The name of the table in the database

    id = db.Column(db.Integer, primary_key=True)  # Unique user ID
    name = db.Column(db.String(100), nullable=False)  # Full name
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email (must be unique)
    password = db.Column(db.String(200), nullable=False)  # Encrypted password

    def __repr__(self):
        return f'<User {self.name}>'

