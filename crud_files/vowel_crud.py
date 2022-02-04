#!/usr/bin/env python3.6
"""Vowel CRUD operations."""


from models.model import db
from models.vowel_model import Vowel

##############################
### VOWEL CRUD FUNCTIONS ###
##############################

def create_vowel(chars, level, origin=None):
    """Create and return a new vowel."""

    vowel = Vowel(chars=chars, level=level, origin=origin)

    db.session.add(vowel)
    db.session.commit()

    return vowel


def get_vowel(chars):
    """Retrieve vowel object."""

    return Vowel.query.filter(Vowel.chars.like(chars)).first()


def get_all_vowels():
    """Return full list of vowel-objects."""

    return Vowel.query.all()

def get_vowels_by_level(level):
    """Return partial list of vowel-objects."""

    return Vowel.query.filter(Vowel.level==level).all()
