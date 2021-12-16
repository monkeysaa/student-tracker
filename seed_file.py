#!/usr/bin/env python3.6
"""Script to seed database."""

import crud
import json
import model
import os
from random import choice, randint
import server


# Switch to Subprocess module or Popen()
os.system('dropdb student-tracker')
os.system('createdb student-tracker')
model.connect_to_db(server.app, 'postgresql:///student-tracker')
model.db.create_all()

# Load student data from JSON file
with open('data/seed_students.json') as f:
    student_data = json.loads(f.read())

# Create students
for student in student_data:
    first_name, last_name, grade = (student['first_name'],
                                    student['last_name'],
                                    student['grade'])

    db_student = crud.create_student(first_name, last_name, grade)

# Load vowel data from JSON file
with open('data/seed_vowels.json') as f2:
    vowel_data = json.loads(f2.read())

# Create and store vowels
vowels_in_db = []

"""
Vowel Level ENUMs: 
0 = Extremes (ee, oo, o)
1 = Short (a, e, i, u)
2 = Final E (structure tbd)
3 = 2VGW (ai, oa, ea)
4 = Other long (ay, ie, oe, ue, ow)
5 = Sliders (ow, ou, oi, oy)
6 = Alternates (aw, au, ew, eu)
7 = Sneaky gh (igh, ough, augh)

Vowel Origin ENUMs:
null = not yet assigned
0 = Old English
1 = Latin
2 = Greek
"""

for vowel in vowel_data:
    char, level, origin = (vowel['char'], vowel['level'], vowel['origin'])

    db_vowel = crud.create_vowel(char, level, origin)
    vowels_in_db.append(db_vowel)

model.db.session.commit()
