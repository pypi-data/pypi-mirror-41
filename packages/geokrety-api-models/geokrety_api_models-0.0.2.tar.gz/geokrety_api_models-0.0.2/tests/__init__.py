import os
import unittest

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session

from geokrety_api_models.base import Base


def setup_module():
    global transaction, connection, engine

    # Connect to the database and create the schema within a transaction
    engine = create_engine(os.environ.get('TEST_DATABASE_URL',
                                          'mysql+mysqldb://root@127.0.0.1/geokrety_unittest?charset=utf8mb4'))
    connection = engine.connect()
    transaction = connection.begin()
    Base.metadata.create_all(connection)
    # If you want to insert fixtures to the DB, do it here


def teardown_module():
    # Roll back the top level transaction and disconnect from the database
    transaction.rollback()
    connection.close()
    engine.dispose()


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.__transaction = connection.begin_nested()
        self.session = Session(connection)

    def tearDown(self):
        self.session.close()
        self.__transaction.rollback()
