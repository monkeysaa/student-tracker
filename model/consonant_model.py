#!/usr/bin/env python3.6
"""Affix Model"""


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
