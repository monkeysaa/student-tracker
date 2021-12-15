"""CRUD testing."""

from crud import *
from model import db, Student, connect_to_db
import unittest

class TestStudentCreation(unittest.TestCase):

    def test_creation(self):
        """Confirms that total increases by 1 after new student created."""

        if get_student_by_name('Test', 'Student'):
            remove_student('Test', 'Student')

        num_students = len(get_all_students())
        create_student('Test', 'Student', 1)
        self.assertEqual(len(get_all_students()), num_students + 1)
    

    def test_duplication(self):
        """Tests duplication error within create_student"""
        create_student('Test', 'Student', 2)
        self.assertEqual(create_student('Test', 'Student', 9), 'Error: Student name already exists.')
    

    def test_update(self):
        """Confirms that update_student changes grade."""

        if get_student_by_name('Test', 'Student'):
            remove_student('Test', 'Student')
        
        student = create_student('Test', 'Student', 3)
        update_student(student.id, 'Test', 'Student', 99)

        self.assertEqual(get_student_by_id(student.id).grade, 99)


    def test_removal(self):
        """Confirms that remove_student deletes student object from db."""

        if not get_student_by_name('Test', 'Student'):
            create_student('Test', 'Student', 4)

        num_students = len(get_all_students())
        remove_student('Test', 'Student')
        self.assertEqual(get_student_by_name('Test', 'Student'), None)
        self.assertEqual(len(get_all_students()), num_students-1)



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    unittest.main(exit=False)

