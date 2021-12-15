"""CRUD operations."""

from model import db, Student, connect_to_db


def create_student(first_name, last_name, grade):
    """Create and return a new student."""

    student = get_student_by_name(first_name, last_name)
    if not student:
        student = Student(first_name=first_name, 
                          last_name=last_name, 
                          grade=grade)

        db.session.add(student)
        db.session.commit()

        return student
    
    else:
        return 'Error: Student name already exists.' 

def update_student(id, f_name, l_name, grade, lvl):
    """Update a new user."""

    student = get_student_by_id(id)
    print('Implement updating feature')

    student.first_name = f_name
    student.last_name = l_name
    student.grade = grade
    student.reading_level = lvl

    db.session.commit()

    return student

def get_student_by_name(f_name, l_name):
    """Retrieve student object by first and last name."""
    
    return Student.query.filter(Student.first_name.like(f_name), Student.last_name.like(l_name)).first()

def get_all_students():
    
    return Student.query.all()

def get_student_by_id(id):
    return Student.query.filter_by(id=id).first()

def remove_student(first_name, last_name):
    student = get_student_by_name(first_name, last_name) 

    if student:
        Student.query.filter_by(id=student.id).delete()
        if not get_student_by_name(first_name, last_name):
            db.session.commit()
            return "Success"
        else:
            return "Error"
    else:
        return "No such student exists"
    

if __name__ == '__main__':
    from server import app
    connect_to_db(app)