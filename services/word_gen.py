# Class: Word Generator
#     Takes in options
#     What level: CVC, Final E, etc
#     Implement
#     Returns word at the end

# service class encapsulates logic for an action
from crud_files import crud, vowel_crud, affix_crud, consonant_crud, student_crud
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

    # assign instance variables to cons_level etc

    def __init__(self, cons_level, vowel_level, word_level):

        self.cons_level = cons_level or 0
        self.vowel_level = vowel_level or 0
        self.word_level = word_level or 0

    #TODO: Once by_levels are working, set cons_level default to highest, and then delete this function
    def generate_random(self):

        vowels = vowel_crud.get_all_vowels()
        consonants = consonant_crud.get_all_consonants()

        vowel = random.choice(vowels).chars
        beg_cons = random.choice(consonant_crud.get_consonants_by_location(0))
        end_cons = random.choice(consonant_crud.get_consonants_by_location(None))

        word = "" + beg_cons.chars + vowel + end_cons.chars

        return word

    def generate_catered_word(self):

        #TODO: Create get_all_vowels_by_level and get_all_consonants_by_level in CRUD
        vowels = vowel_crud.get_all_vowels_by_level()
        consonants = consonant_crud.get_all_consonants_by_level()

    def __repr__(self):
        return f"{self.word}"

