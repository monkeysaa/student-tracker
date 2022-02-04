#!/usr/bin/env python3.6
"""Server for pseudowords app."""

from crud_files import crud, vowel_crud, affix_crud, consonant_crud, student_crud
from flask import Flask, render_template, request, session, redirect, jsonify
from models.model import connect_to_db, app
import pprint
import random
from services import word_gen

# app = Flask(__name__)


@app.route('/')
def homepage():
    """Show homepage."""

    vowels = vowel_crud.get_all_vowels()
    consonants = consonant_crud.get_all_consonants()

    vowel = random.choice(vowels).chars
    beg_cons = random.choice(consonant_crud.get_consonants_by_location(0))
    end_cons = random.choice(consonant_crud.get_consonants_by_location(None))

    word = "" + beg_cons.chars + vowel + end_cons.chars
    # print(word)

    return render_template('homepage.html', word=word)


@app.route('/vowels')
def all_vowels():
    """View all vowels."""

    vowels = vowel_crud.get_all_vowels()

    return render_template('vowels.html', vowels=vowels)


@app.route('/consonants')
def all_cons():
    """View all consonants."""

    consonants = consonant_crud.get_all_consonants()

    return render_template('consonants.html', consonants=consonants)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
