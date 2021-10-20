"""Pseudowords

The front-end for a database that allows users to track students' decoding 
progress, and to create pseudoword sets catered to their reading levels.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///student-tracker'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

def get_student_by_first_name(first_name):
    """Given a first name, print info about the matching student."""

    QUERY = """
        SELECT first_name, last_name, reading_level
        FROM students
        WHERE first_name = :first_name
        """
    
        db_cursor = db.session.execute(QUERY, {'github': github})

    row = db_cursor.fetchone()

    print(f"Student: {row[0]} {row[1]}\nReading level: {row[2]}")

    return row
