"""Habit Tracker Web Server entry point."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../habit_tracker.db'
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    """Adding Docstring to satisfy github actions."""
    return 'Hello, World!!!'


@app.route('/team/<member>')  # i.e /team/daniel
def team_page(member):
    """Route for team members.

    Each member is associated with their own route.
    """
    if member == "daniel":
        return "Daniel's page!"
    else:
        return "Unknown team member: {}".format(member)


if __name__ == '__main__':
    app.run()
