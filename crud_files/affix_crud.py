#!/usr/bin/env python3.6
"""Affix CRUD operations."""

from model import db, Affix, connect_to_db


def create_affix(affix, prefix):
    """Create and return a new consonant."""

    affix = Affix(affix=affix, prefix=prefix)

    db.session.add(affix)
    db.session.commit()

    return affix


def get_affix(affix):
    """Retrieve affix object by name."""

    return Affix.query.filter(Consonant.affix.like(affix)).first()


def get_all_affixes():
    """Return full list of affix-objects."""

    return Affix.query.all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
