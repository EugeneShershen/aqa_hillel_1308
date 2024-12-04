import logging
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lesson_29.src.db_tables import Base


class DataBase:
    """Base class for database.
    """
    __DATABASE_URL = "postgresql://test_user:test_password@localhost:5432/test_db"

    def __init__(self):
        try:
            self.logger = logging.getLogger(self.__class__.__name__)

            self.logger.info('Connecting to the database')
            self.engine = create_engine(self.__DATABASE_URL)

            self.logger.info('Creating session with database')
            Session = sessionmaker(bind=self.engine, autoflush=False)
            self.session = Session()

        except (Exception, psycopg2.Error) as error:
            self.logger.error(str(error))

    def create_tables(self):
        """Creates tables into the database.
        """
        try:
            self.logger.info('Creating tables for database')
            Base.metadata.create_all(self.engine)

        except (Exception, psycopg2.Error) as error:
            self.logger.error(str(error))
