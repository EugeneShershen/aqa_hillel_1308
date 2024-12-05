import allure
from assertpy import assert_that

from lesson_29.src.database import DataBase


class AssertionsDatabase:
    db = DataBase()

    @allure.step("Assert that connection was created")
    def assert_connection(self, connection):
        self.db.logger.info("Asserting that connection was created")
        assert_that(connection).is_not_equal_to(None)
