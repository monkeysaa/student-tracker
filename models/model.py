#!/usr/bin/env python3.6
"""Pseudowords Model

The model for a database that allows users to track students' decoding
progress, and to create pseudoword sets catered to their reading levels.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from server import app
from flask_migrate import Migrate


app = Flask(__name__, template_folder='/home/vagrant/src/pseudowords/templates')
db = SQLAlchemy()
migrate = Migrate(app, db)

# located below db definition, since models require db to exist already
from models.vowel_model import Vowel
from models.student_model import Student
from models.consonant_model import Consonant
from models.affix_model import Affix


class Student_Vowels(db.Model):

    __tablename__ = 'student_vowels'

    student_id = db.Column(db.Integer,
                       db.ForeignKey('students.id'),
                       primary_key=True
                       )
    vowel_id = db.Column(db.Integer,
                          db.ForeignKey('vowels.id'),
                          primary_key=True
                          )
    student = db.relationship('Student', backref='vowels')
    vowel = db.relationship('Vowel')

    def __repr__(self):
        return f'<Assoc {self.student.first_name} reads {self.vowel.chars}>'


class Student_Consonants(db.Model):

    __tablename__ = 'student_consonants'

    student_id = db.Column(db.Integer,
                       db.ForeignKey('students.id'),
                       primary_key=True
                       )
    cons_id = db.Column(db.Integer,
                          db.ForeignKey('consonants.id'),
                          primary_key=True
                          )
    student = db.relationship('Student', backref='consonants')
    consonant = db.relationship('Consonant')

    def __repr__(self):
        return f'<Assoc {self.student.first_name} reads {self.consonant.chars}>'


class Student_Affixes(db.Model):

    __tablename__ = 'student_affixes'

    student_id = db.Column(db.Integer,
                       db.ForeignKey('students.id'),
                       primary_key=True
                       )
    affix_id = db.Column(db.Integer,
                          db.ForeignKey('affixes.id'),
                          primary_key=True
                          )
    student = db.relationship('Student', backref='affixes')
    affix = db.relationship('Affix')

    def __repr__(self):
        return f'<Assoc {self.student.first_name} reads {self.affixes.affix}>'


"""
Attempted consonant sequence
1. no-blends or hardsoft,
2. blends+location=1
3. blends+location=2
4. no-blends+hardsoft+location=2
5. blends=1
6. one blend
7. all
"""


def connect_to_db(app, db_uri='postgresql:///student-tracker'):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app, 'postgresql:///student-tracker')
