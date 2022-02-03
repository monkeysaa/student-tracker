#!/usr/bin/env python3.6
"""Affix Model"""


class Affix(db.Model):
    """Prefixes and Suffixes."""

    __tablename__ = 'affixes'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    affix = db.Column(db.String, nullable=False)
    location = db.Column(db.Integer) # None = N/A, 0 = beginning, 1 = end

    def __repr__(self):
        return f'<Affix {self.affix}>'
