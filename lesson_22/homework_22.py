import psycopg2
from sqlalchemy.orm import sessionmaker

from lesson_22.tables_for_db import engine, Course, Student, RegistrationList


def create_session():
    """ Creates and closes a database session.
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    return session


def session_decorator(func):
    """ Decorator for creating and closing session while performing actions with database.
    """
    def wrapper(*args, **kwargs):
        session = create_session()
        result = func(session, *args, **kwargs)
        session.close()
        return result
    return wrapper


@session_decorator
def add_course(session, name: str):
    """ Adds a new object "Course" to the database.

    :param session: session for performing actions with database
    :param name: name for the new object
    """
    try:
        new_course = Course(name=name)
        session.add(new_course)
        session.commit()
        print(f"Course '{name}' was successfully added")

    except (Exception, psycopg2.Error) as error:
        print(error)


@session_decorator
def add_student(session, name: str, age: int, courses: list[str]):
    """ Adds a new object "Student" to the database.

    :param session: session for performing actions with database
    :param name: name for the new object
    :param age: age for the new object
    :param courses: list of courses for the new object
    """
    try:
        new_student = Student(name=name, age=age)
        session.add(new_student)

        for course in courses:
            course_obj = session.query(Course).filter_by(name=course).first()

            if course_obj is None:
                raise TypeError(f"Course '{course}' does not exist")

            new_registration = RegistrationList(student=new_student,
                                                course=course_obj)
            session.add(new_registration)

        session.commit()
        print(f"Student '{name}' was successfully added")

    except (Exception, psycopg2.Error) as error:
        print(f'Error: {error}')


@session_decorator
def update_course(session, course_name: str, updated_name: str):
    """ Updates an information about a certain object "Course".

    :param session: session for performing actions with database
    :param course_name: name of the course you want to update
    :param updated_name: new name for the chosen course
    """
    try:
        course_obj = session.query(Course).filter_by(name=course_name).first()

        if course_obj:
            course_obj.name = updated_name
            session.commit()

            print(f"Course '{course_name}' was successfully updated")

        else:
            raise Exception(f"Course '{course_name}' does not exist")

    except (Exception, psycopg2.Error) as error:
        print(f'Error: {error}')


@session_decorator
def update_student(session, student_id: int, updated_name: str = None, updated_age: int = None):
    """ Updates an information about a certain object "Student".

    :param session: session for performing actions with database
    :param student_id: id of the student you want to update
    :param updated_name: new name for the chosen student
    :param updated_age: new age for the chosen student
    """
    try:
        student_obj = session.query(Student).filter_by(id=student_id).first()

        if student_obj:
            if updated_name is not None:
                student_obj.name = updated_name

            if updated_age is not None:
                student_obj.age = updated_age

            session.commit()

            print(f"Student with an id '{student_id}' was successfully updated")

        else:
            raise Exception(f"Student with an id '{student_id}' does not exist")

    except (Exception, psycopg2.Error) as error:
        print(f'Error: {error}')


@session_decorator
def delete_course(session, course_name: str):
    """ Deletes a certain object "Course" from the database.

    :param session: session for performing actions with database
    :param course_name: name of the course you want to delete
    """
    try:
        course_obj = session.query(Course).filter_by(name=course_name).first()

        if course_obj:
            session.query(RegistrationList).filter_by(id_course=course_obj.id).delete()
            session.delete(course_obj)
            session.commit()

            print(f"Course '{course_name}' was successfully deleted")

        else:
            raise Exception(f"Course '{course_name}' does not exist")

    except (Exception, psycopg2.Error) as error:
        print(f'Error: {error}')


@session_decorator
def delete_student(session, student_id: int):
    """ Deletes a certain object "Student" from the database.

    :param session: session for performing actions with database
    :param student_id: id of the student you want to delete
    """
    try:
        student_obj = session.query(Student).filter_by(id=student_id).first()

        if student_obj:
            session.query(RegistrationList).filter_by(id_student=student_id).delete()
            session.delete(student_obj)
            session.commit()

            print(f"Student with an id '{student_id}' was successfully deleted")

        else:
            raise Exception(f"Student with an id '{student_id}' does not exist")

    except (Exception, psycopg2.Error) as error:
        print(f'Error: {error}')


@session_decorator
def student_list_of_certain_course(session, course_name: str):
    """ Prints and returns a list of students by the specified course name.

    :param session: session for performing actions with database
    :param course_name: name of the course you want to search for
    """
    try:
        course_obj = session.query(Course).filter_by(name=course_name).first()

        if course_obj is None:
            raise TypeError(f"Course '{course_name}' does not exist")

        response = (session.query(Student.name, Student.age)
                    .join(RegistrationList, Student.id == RegistrationList.id_student)
                    .join(Course, Course.id == RegistrationList.id_course)
                    .filter_by(name=course_name)
                    .all())

        print(f"List of students on the course '{course_name}':")
        for name, age in response:
            print(f"Name: {name}   Age: {age}")

        return response

    except (Exception, psycopg2.Error) as error:
        print(f'Error: {error}')


@session_decorator
def course_list_of_certain_student(session, student_id: int):
    """ Prints and returns a list of courses by the specified student id.

    :param session: session for performing actions with database
    :param student_id: id of the student you want to search for
    """
    try:
        student_obj = session.query(Student).filter_by(id=student_id).first()

        if student_obj is None:
            raise TypeError(f"Student with an id '{student_id}' does not exist")

        response = (session.query(Course.name)
                    .join(RegistrationList, Course.id == RegistrationList.id_course)
                    .join(Student, Student.id == RegistrationList.id_student)
                    .filter_by(id=student_id)
                    .all())

        print(f"List of courses of a student with an id '{student_id}':")
        for name in response:
            str_name = ','.join(name)
            print(f"Name: {str_name}")

        return response

    except (Exception, psycopg2.Error) as error:
        print(f'Error: {error}')
