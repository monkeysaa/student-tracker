# Class: Word Generator
#     Takes in options
#     What level: CVC, Final E, etc
#     Implement
#     Returns word at the end

# service class encapsulates logic for an action
from crud_files import crud
import random

class Word_Generator():
    """Creates a word or pseudoword based on the parameters passed.

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

    def __init__(self, cons_level, vowel_level, word_level):

        # Default = CVC
        vowels = vowel_crud.get_all_vowels()
        consonants = consonant_crud.get_all_consonants()

        vowel = random.choice(vowels).chars
        beg_cons = random.choice(consonant_crud.get_consonants_by_location(0))
        end_cons = random.choice(consonant_crud.get_consonants_by_location(1))

        word = "" + beg_cons.chars + vowel + end_cons.chars

    def __repr__(self):
        return f"{self.word}"

