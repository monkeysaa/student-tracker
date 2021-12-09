"""Pseudowords

The front-end for a database that allows users to track students' decoding 
progress, and to create pseudoword sets catered to their reading levels.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


class Student(db.Model):
    """A student."""

    __tablename__ = 'students'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    grade = db.Column(db.Integer)
    reading_level = db.Column(db.String)
    # prefixes - A list of prefixes for this student to practice
    # suffixes - A list of suffixes for this student to practice


    def __repr__(self):
        return f'<Student f_name={self.first_name} l_name={self.last_name}>'


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///student-tracker'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
