import allure
from pytest import mark

from lesson_29.src.course_table import CourseTable
from lesson_29.data.tests_data_cud import courses_cud
from lesson_29.data.tests_data_search import courses_search
from lesson_29.src.assertions.assetions_course_table import AssertionsCourseTable


@allure.feature("Table 'Course'")
class TestCourseTable:
    """Test-class for 'Course' table of the database.
    """
    ct = CourseTable()
    assertion = AssertionsCourseTable()

    @allure.title('Add')
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

        self.assertion.assert_add(received_name, name)

    @allure.title('Update')
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

        self.assertion.assert_update(received_name, new_name)

    @allure.title('Delete')
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

        self.assertion.assert_delete(name)

    @allure.title('Get courses by student id')
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

        self.assertion.assert_get_courses_by_student_id(result, course_info)
