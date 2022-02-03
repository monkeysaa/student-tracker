#!/usr/bin/env python3.6
"""Affix CRUD operations."""


from models.model import db, connect_to_db
from models.affix_model import Affix

##############################
### AFFIX CRUD FUNCTIONS ###
##############################

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
