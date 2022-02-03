#!/usr/bin/env python3.6
"""Pseudowords Model

The model for a database that allows users to track students' decoding
progress, and to create pseudoword sets catered to their reading levels.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.vowel_model import Vowel

app = Flask(__name__)
db = SQLAlchemy()


class Student(db.Model):
    """A student."""

    __tablename__ = 'students'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer)
    v_level = db.Column(db.Integer) # 1. short, 2. v+e, 3. both, 4. 2vgw, 5. 1-4 mix, 6. sliders, 7. 1-6 mix, 8. gh
    c_level = db.Column(db.Integer)
    a_level = db.Column(db.Boolean)

    # affixes - Associated prefixes and suffixes
    # vowels - Associated vowels
    # consonants - Associated consonants? or consonant-levels?

    def __repr__(self):
        return f'<Student {self.id}: {self.first_name} {self.last_name}>'


# class Vowel(db.Model):
#     """A vowel sound.

#     Vowel Level ENUMs:
#         0 = Extremes (ee, oo, o)
#         1 = Short Vowels (a, e, i, u)
#         2 = Final E (structure tbd)
#         3 = 2VGW (ai, oa, ea)
#         4 = Other Long (ay, ie, oe, ue, ow)
#         5 = Sliders (ow, ou, oi, oy)
#         6 = Alternates (aw, au, ew, eu)
#         7 = GH (igh, ough, augh)

#     Vowel Origin ENUMs:
#         null = not yet assigned
#         0 = Old English
#         1 = Latin
#         2 = Greek
#     """

#     __tablename__ = 'vowels'

#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     chars = db.Column(db.String(5), nullable=False)
#     level = db.Column(db.Integer, nullable=False)
#     origin = db.Column(db.Integer) # Int if ENUM

#     def __repr__(self):
#         return f'<Vowel {self.chars}>'


class Consonant(db.Model):
    """A consonant or consonant blend.

    Complex_c:
    - c and g - which vary depending on whether they're followed by e, i, or y
    - two-letter consonant digraphs such as sh, ch, th, wh, and ng

    Location ENUMs:
        null (default) = not specified
        0 = beginning of word
        1 = end of word

    Blend:
        False (default) = consonant stands alone
        True = consonant characters form a blend


    Blocker
        False (default) = no limitation of vowels
        True = only paired with short vowels.

    Consonant Level ENUMs:
        0 = no blockers, no blends, no complex_c
        1 = no blends, no complex_c
        2 = no blends
        3 = initial blends
        4 = final blends
    """

    __tablename__ = 'consonants'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    chars = db.Column(db.String(3), nullable=False)
    complex_c = db.Column(db.Boolean, nullable=False)
    location = db.Column(db.Integer) # None = N/A, 0 = beginning, 1 = end
    blend = db.Column(db.Boolean, nullable=False)
    blocker = db.Column(db.Boolean, nullable=False)
    level = db.Column(db.Integer)

    def __repr__(self):
        return f'<Cons {self.chars}>'


class Affix(db.Model):
    """Prefixes and Suffixes."""

    __tablename__ = 'affixes'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    affix = db.Column(db.String, nullable=False)
    location = db.Column(db.Integer) # None = N/A, 0 = beginning, 1 = end

    def __repr__(self):
        return f'<Affix {self.affix}>'


# class Student_Vowels(db.Model):

#     __tablename__ = 'student_vowels'

#     student_id = db.Column(db.Integer,
#                        db.ForeignKey('students.id'),
#                        primary_key=True
#                        )
#     vowel_id = db.Column(db.Integer,
#                           db.ForeignKey('vowels.id'),
#                           primary_key=True
#                           )
#     student = db.relationship('Student', backref='vowels')
#     vowel = db.relationship('Vowel')

#     def __repr__(self):
#         return f'<Assoc {self.student.first_name} reads {self.vowel.chars}>'


# class Student_Consonants(db.Model):

#     __tablename__ = 'student_consonants'

#     student_id = db.Column(db.Integer,
#                        db.ForeignKey('students.id'),
#                        primary_key=True
#                        )
#     cons_id = db.Column(db.Integer,
#                           db.ForeignKey('consonants.id'),
#                           primary_key=True
#                           )
#     student = db.relationship('Student', backref='consonants')
#     consonant = db.relationship('Consonant')

#     def __repr__(self):
#         return f'<Assoc {self.student.first_name} reads {self.consonant.chars}>'


# class Student_Affixes(db.Model):

#     __tablename__ = 'student_affixes'

#     student_id = db.Column(db.Integer,
#                        db.ForeignKey('students.id'),
#                        primary_key=True
#                        )
#     affix_id = db.Column(db.Integer,
#                           db.ForeignKey('affixes.id'),
#                           primary_key=True
#                           )
#     student = db.relationship('Student', backref='affixes')
#     affix = db.relationship('Affix')

#     def __repr__(self):
#         return f'<Assoc {self.student.first_name} reads {self.affixes.affix}>'


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
