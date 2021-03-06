"""Databse ORM models."""
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """Database ORM model representing a User."""

    __tablename__ = "users"
    username = db.Column(db.String, primary_key=True)
    hashed_password = db.Column(db.String)

    def set_password(self, password):
        """Set hashed password for a user.

        :param password str: password to hash and set.
        """
        self.hashed_password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check that hashed password matches expected hashed password.

        :param password str: password to check
        """
        return check_password_hash(self.hashed_password, password)

    def get_id(self):
        """Get unique id of user (just the username).

        :return str: user id
        """
        return self.username


class UserHabit(db.Model):
    """Database ORM model representing a single user habit."""

    __tablename__ = "user_habits"
    username = db.Column(db.String, primary_key=True)
    habitname = db.Column(db.String, primary_key=True)


class UserActivity(db.Model):
    """Database ORM model representing a single activity."""

    __tablename__ = "user_activities"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    habitname = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
