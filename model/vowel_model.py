#!/usr/bin/env python3.6
"""Vowel Model"""


class Vowel(db.Model):
    """A vowel sound.

    Vowel Level ENUMs:
        0 = Extremes (ee, oo, o)
        1 = Short Vowels (a, e, i, u)
        2 = Final E (structure tbd)
        3 = 2VGW (ai, oa, ea)
        4 = Other Long (ay, ie, oe, ue, ow)
        5 = Sliders (ow, ou, oi, oy)
        6 = Alternates (aw, au, ew, eu)
        7 = GH (igh, ough, augh)

    Vowel Origin ENUMs:
        null = not yet assigned
        0 = Old English
        1 = Latin
        2 = Greek
    """

    __tablename__ = 'vowels'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    chars = db.Column(db.String(5), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    origin = db.Column(db.Integer) # Int if ENUM

    def __repr__(self):
        return f'<Vowel {self.chars}>'

