"""CRUD operations."""

from model import db, Student, connect_to_db


def create_student(first_name, last_name, grade, reading_level):
    """Create and return a new student."""

    student = Student(first_name=first_name, last_name=last_name, grade=grade,
                      reading_level=reading_level)

    db.session.add(student)
    db.session.commit()

    return student


def get_student_by_name(first_name, last_name):

    return student

def get_student_by_name(first_name, last_name):
    """Given a student's name, print info about the matching student."""

    QUERY = """
        SELECT first_name, last_name, grade, reading_level
        FROM students
        WHERE first_name = :first_name
        """

    db_cursor = db.session.execute(QUERY, {'first_name': first_name})

    row = db_cursor.fetchone()

    print(f"Student: {row[0]} {row[1]}\nGrade: {row[2]}")

    return row


def update_student(first_name, last_name, grade, reading_level):
    """Update a new user."""

    # student = Student(first_name=first_name, last_name=last_name, grade=grade,
    #                   reading_level=reading_level)

    # db.session.add(student)
    db.session.commit()

    return student

def delete_student(first_name, last_name):

    return None

if __name__ == '__main__':
    from server import app
    connect_to_db(app)