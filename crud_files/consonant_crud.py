#!/usr/bin/env python3.6
"""Consonant CRUD operations."""

from model import db, Consonant, connect_to_db


def create_consonant(chars, complex_c, location, blend, blocker):
    """Create and return a new consonant."""

    consonant = Consonant(chars=chars, complex_c=complex_c,
                          location=location, blend=blend, blocker=blocker)

    db.session.add(consonant)
    level = None
    """
        Consonant Level ENUMs:
            0 = no blockers, no blends, no complex_c
            1 = no blends, no complex_c
            2 = no blends
            3 = initial blends
            4 = final blends
    """

    if blend:
        if location == 0:
            level = 3
        else:
            level = 4

    else:
        if complex_c:
            level = 2
        elif blocker:
            level = 1
        else:
            level = 0
    consonant.level = level

    db.session.commit()

    return consonant


def get_consonant(chars):
    """Retrieve consonant object."""

    return Consonant.query.filter(Consonant.chars.like(chars)).first()


def get_all_consonants():
    """Return full list of consonant-objects."""

    return Consonant.query.all()

def get_consonants_by_location(loc):
    """Return partial list of consonant-objects."""

    return Consonant.query.filter(Consonant.location==loc).all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
