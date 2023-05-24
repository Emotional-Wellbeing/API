import json
import unittest
from pathlib import Path
from src.validator.user_data_validator import UserDataValidator


class TestUserDataValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.udv = UserDataValidator()
        self.basepath = Path(__file__).parent / '../json'

    def testValidatorNoUserId(self):
        path = self.basepath / 'user_data_no_user_id.json'
        with path.open() as json_file:
            data = json.load(json_file)
        self.assertFalse(self.udv.validate(data), "No user id provided")

    def testValidatorEmptyData(self):
        path = self.basepath / 'user_data_empty_data.json'
        with path.open() as json_file:
            data = json.load(json_file)
        self.assertTrue(self.udv.validate(data), "No data provided")

    def testValidatorFullData(self):
        path = self.basepath / 'user_data_full_data.json'
        with path.open() as json_file:
            data = json.load(json_file)
        self.assertTrue(self.udv.validate(data), "Full data provided")

    def testValidatorOneData(self):
        path = self.basepath / 'user_data_one_data.json'
        with path.open() as json_file:
            data = json.load(json_file)
        self.assertTrue(self.udv.validate(data), "One data provided")

    def testValidatorWrongFirstLevel(self):
        path = self.basepath / 'user_data_wrong_first_level.json'
        with path.open() as json_file:
            data = json.load(json_file)
        self.assertFalse(self.udv.validate(data), "Wrong data provided at first level")

    def testValidatorWrongSecondLevel(self):
        path = self.basepath / 'user_data_wrong_second_level.json'
        with path.open() as json_file:
            data = json.load(json_file)
        self.assertFalse(self.udv.validate(data), "Wrong data provided at second level")

    def testValidatorWrongThirdLevelLeave(self):
        path = self.basepath / 'user_data_wrong_third_level_leave.json'
        with path.open() as json_file:
            data = json.load(json_file)
        self.assertFalse(self.udv.validate(data), "Wrong data provided at third level")

    def testValidatorWrongThirdLevelNonLeave(self):
        path = self.basepath / 'user_data_wrong_third_level_non_leave.json'
        with path.open() as json_file:
            data = json.load(json_file)
        self.assertFalse(self.udv.validate(data), "Wrong data provided at third level")

    def testValidatorWrongFourthLevel(self):
        path = self.basepath / 'user_data_wrong_fourth_level.json'
        with path.open() as json_file:
            data = json.load(json_file)
        self.assertFalse(self.udv.validate(data), "Wrong data provided at fourth level")


if __name__ == '__main__':
    unittest.main()
