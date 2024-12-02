from assertpy import assert_that

from lesson_29.src.database import DataBase


class TestDataBase:
    """Test-class for basic actions with database.
    """

    def test_db_connection(self):
        """Tests connection with database.
        """
        connection = None
        try:
            connection = DataBase().engine.connect()
            assert_that(connection).is_not_equal_to(None)
        finally:
            if connection:
                connection.close()
