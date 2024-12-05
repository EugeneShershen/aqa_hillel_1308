import allure

from lesson_29.src.database import DataBase
from lesson_29.src.assertions.assertions_database import AssertionsDatabase


@allure.feature("Basic Database actions")
class TestDataBase:
    """Test-class for basic actions with database.
    """
    assertion = AssertionsDatabase()

    @allure.title("Connection")
    def test_db_connection(self):
        """Tests connection with database.
        """
        connection = None
        try:
            connection = DataBase().engine.connect()
            self.assertion.assert_connection(connection)
        finally:
            if connection:
                connection.close()
