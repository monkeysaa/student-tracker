"""CRUD testing."""

from crud import create_student
from model import db, Student, connect_to_db
import unittest

class TestStudentCreation(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

# class TestQuery(unittest.TestCase):
#     def setUp(self):
#         self.engine = create_engine('sqlite:///:memory:')
#         self.session = Session(engine)
#         Base.metadata.create_all(self.engine)
#         self.panel = Panel(1, 'ion torrent', 'start')
#         self.session.add(self.panel)
#         self.session.commit()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
