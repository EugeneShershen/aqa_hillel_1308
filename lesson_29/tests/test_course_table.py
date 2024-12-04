from pytest import mark, raises
from assertpy import assert_that

from lesson_29.src.course_table import CourseTable
from lesson_29.data.tests_data_cud import courses_cud
from lesson_29.data.tests_data_search import courses_search


class TestCourseTable:
    """Test-class for 'Course' table of the database.
    """
    ct = CourseTable()

    @mark.parametrize('course', [
        courses_cud[1],
        courses_cud[2],
        courses_cud[3]
    ])
    def test_add_course(self, course):
        """Tests adding a course.
        """
        name = course['old_name']

        self.ct.add_course(name=name)
        received_name = self.ct.get_course_name_by_name(name)

        assert_that(received_name).is_equal_to(name)

    @mark.parametrize('course', [
        courses_cud[1],
        courses_cud[2],
        courses_cud[3]
    ])
    def test_update_course(self, course):
        """Tests updating a course.
        """
        old_name = course['old_name']
        new_name = course['new_name']

        self.ct.update_course(course_name=old_name, updated_name=new_name)
        received_name = self.ct.get_course_name_by_name(new_name)

        assert_that(received_name).is_equal_to(new_name)

    @mark.parametrize('course', [
        courses_cud[1],
        courses_cud[2],
        courses_cud[3]
    ])
    def test_delete_course(self, course):
        """Tests deleting a course.
        """
        name = course['new_name']

        self.ct.delete_course(course_name=name)

        with raises(TypeError):
            self.ct.get_course_name_by_name(name)

    @mark.parametrize('course', [
        courses_search[1],
        courses_search[2],
        courses_search[3]
    ])
    def test_course_list_of_certain_student(self, course):
        """Tests getting a list of courses by student id.
        """
        student_id = course['student_id']
        course_info = course['course_info']

        result = self.ct.course_list_of_certain_student(student_id=student_id)

        assert_that(result).is_equal_to(course_info)
