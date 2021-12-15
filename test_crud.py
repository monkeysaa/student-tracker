"""CRUD testing."""

from crud import *
from model import db, Student, connect_to_db
import unittest

class TestStudentCreation(unittest.TestCase):
    
    def test_duplication(self):
        create_student('Test', 'Student', 9)
        self.assertEqual(create_student('Test', 'Student', 9), 'Error: Student name already exists.')

    def test_creation(self):
        """Confirms that total increases by 1 after new student created."""

        if get_student_by_name('Test', 'Student'):
            remove_student('Test', 'Student')

        num_students = len(get_all_students())
        create_student('Test', 'Student', 18)
        self.assertEqual(len(get_all_students()), num_students + 1)
    
    def test_update(self):

        if get_student_by_name('Test', 'Student'):
            remove_student('Test', 'Student')
        
        student = create_student('Test', 'Student', 1)
        update_student(student.id, 'Test', 'Student', 99)

        self.assertEqual(student.grade, 99)


    
        


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    unittest.main(exit=False)

