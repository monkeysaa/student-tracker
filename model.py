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
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer)
    v_level = db.Column(db.Integer) # 1. short, 2. v+e, 3. both, 4. 2vgw, 5. 1-4 mix, 6. sliders, 7. 1-6 mix, 8. gh
    c_level = db.Column(db.Integer) 

    # affixes - Associated prefixes and suffixes 
    # vowels - Associated vowels
    # consonants - Associated consonants? or consonant-levels? 

    def __repr__(self):
        return f'<Student {self.id}: {self.first_name} {self.last_name}>'


class Vowel(db.Model):
    """A vowel sound."""

    __tablename__ = 'vowels'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    chars = db.Column(db.String)
    level = db.Column(db.Integer)
    origin = db.Column(db.Integer) # Int if ENUM, else String with limit

    def __repr__(self):
        return f'<Vowel {self.chars}>'


class Consonant(db.Model):
    """A consonant or consonant blend."""

    __tablename__ = 'consonants'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    chars = db.Column(db.String, nullable=False)
    hardsoft = db.Column(db.Boolean)
    location = db.Column(db.String) # None is none specified, 1 is beginning, 2 is ending
    blend = db.Column(db.Boolean) 

    def __repr__(self):
        return f'<Cons {self.chars}>'


class Affix(db.Model):
    """Prefixes and Suffixes."""

    __tablename__ = 'affixes'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    affix = db.Column(db.String, nullable=False)
    location = db.Column(db.String) # None is none specified, 1 is beginning, 2 is ending

    def __repr__(self):
        return f'<Affix {self.affix}>'


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
