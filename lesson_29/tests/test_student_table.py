from pytest import mark, raises
from assertpy import assert_that

from lesson_29.src.student_table import StudentTable
from lesson_29.data.tests_data_cud import students_cud
from lesson_29.data.tests_data_search import students_search


class TestCourseTable:
    """Test-class for 'Student' table of the database.
    """
    st = StudentTable()

    @mark.parametrize('student', [
        students_cud[1],
        students_cud[2],
        students_cud[3]
    ])
    def test_add_student(self, student):
        """Tests adding a student.
        """
        name = student['old_name']
        age = student['old_age']
        courses = student['courses']

        self.st.add_student(name=name, age=age, courses=courses)
        student_id = self.st.get_student_id_by_name_age(name, age)
        received_name = self.st.get_student_name_by_id(student_id)

        assert_that(received_name).is_equal_to(name)

    @mark.parametrize('student', [
        students_cud[1],
        students_cud[2],
        students_cud[3]
    ])
    def test_update_student(self, student):
        """Tests updating a student.
        """
        old_name = student['old_name']
        new_name = student['new_name']
        old_age = student['old_age']
        new_age = student['new_age']

        student_id = self.st.get_student_id_by_name_age(old_name, old_age)
        self.st.update_student(student_id=student_id, updated_name=new_name, updated_age=new_age)
        received_name = self.st.get_student_name_by_id(student_id)

        assert_that(received_name).is_equal_to(new_name)

    @mark.parametrize('student', [
        students_cud[1],
        students_cud[2],
        students_cud[3]
    ])
    def test_delete_student(self, student):
        """Tests deleting a student.
        """
        new_name = student['new_name']
        new_age = student['new_age']

        student_id = self.st.get_student_id_by_name_age(new_name, new_age)
        self.st.delete_student(student_id=student_id)

        with raises(TypeError):
            self.st.get_student_name_by_id(student_id)

    @mark.parametrize('student', [
        students_search[1],
        students_search[2],
        students_search[3]
    ])
    def test_student_list_of_certain_course(self, student):
        """Tests for getting a list of students by the course`s name.
        """
        course_name = student['course_name']
        student_info = student['student_info']

        result = self.st.student_list_of_certain_course(course_name=course_name)

        assert_that(result).is_equal_to(student_info)
