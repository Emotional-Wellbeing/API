import json
import unittest

from pathlib import Path

from database import Database


class TestDatabase(unittest.TestCase):

    def setUp(self) -> None:
        self.database = Database(database="test")

    def testSingleton(self):
        self.assertIs(self.database, Database(), "Database instance must be unique")

        # Sanity check - a non-singleton class should create two separate instances
        class NonSingleton:
            pass

        self.assertIsNot(NonSingleton(), NonSingleton(), "In normal class two instances must be different")

    def testInsertUserData(self):
        path = Path(__file__).parent / '../json/input' / 'user_data_full_data.json'
        with path.open() as json_file:
            data = json.load(json_file)
        response = self.database.insert_user_data(data)
        self.assertTrue(response.acknowledged, "ACK must be positive")
        self.assertIsNotNone(response.inserted_id, "Id must be not none")

    def testInsertUserDataBg(self):
        path = Path(__file__).parent / '../json/input' / 'user_data_full_data.json'
        with path.open() as json_file:
            databg = json.load(json_file)
        response = self.database.insert_user_databg(databg)
        self.assertTrue(response.acknowledged, "ACK must be positive")
        self.assertIsNotNone(response.inserted_id, "Id must be not none")
