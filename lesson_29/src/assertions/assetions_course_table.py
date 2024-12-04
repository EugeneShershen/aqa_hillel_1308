import allure
from assertpy import assert_that
from pytest import raises

from lesson_29.src.course_table import CourseTable


class AssertionsCourseTable:
    ct = CourseTable()

    @allure.step("Assert that course was added")
    def assert_add(self, received_name, name):
        self.ct.logger.info("Asserting that course was added")
        assert_that(received_name).is_equal_to(name)

    @allure.step("Assert that course was updated")
    def assert_update(self, received_name, new_name):
        self.ct.logger.info("Asserting that course was updated")
        assert_that(received_name).is_equal_to(new_name)

    @allure.step("Assert that course was deleted")
    def assert_delete(self, name):
        self.ct.logger.info("Asserting that course was deleted")
        with raises(TypeError):
            self.ct.get_course_name_by_name(name)

    @allure.step("Assert that courses was gotten by student id")
    def assert_get_courses_by_student_id(self, result, course_info):
        self.ct.logger.info("Asserting that courses was gotten by student id")
        assert_that(result).is_equal_to(course_info)
