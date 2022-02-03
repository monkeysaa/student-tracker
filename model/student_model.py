#!/usr/bin/env python3.6
"""Student Model"""


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
