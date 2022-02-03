#!/usr/bin/env python3.6
"""Server for pseudowords app."""

import crud
from flask import Flask, render_template, request, session, redirect, jsonify
from model import connect_to_db
import pprint
import random

app = Flask(__name__)


@app.route('/')
def homepage():
    """Show homepage."""

    vowels = crud.get_all_vowels()
    consonants = crud.get_all_consonants()

    vowel = random.choice(vowels).chars
    beg_cons = random.choice(crud.get_consonants_by_location(0))
    end_cons = random.choice(crud.get_consonants_by_location(1))

    word = "" + beg_cons.chars + vowel + end_cons.chars 
    print(word)

    return render_template('homepage.html', word=word)


@app.route('/vowels')
def all_vowels():
    """View all vowels."""

    vowels = crud.get_all_vowels()

    return render_template('vowels.html', vowels=vowels)


@app.route('/consonants')
def all_cons():
    """View all consonants."""

    consonants = crud.get_all_consonants()

    return render_template('consonants.html', consonants=consonants)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)