import json
import unittest
from pathlib import Path

from validator.user_data_validator import UserDataValidator


class TestUserDataValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.udv = UserDataValidator()
        self.base_path = Path(__file__).parent / '../json/input'

    def __doTrueTest(self, input_path, text):
        with input_path.open() as json_file:
            input_data = json.load(json_file)
        self.assertTrue(self.udv.validate(input_data), text)

    def __doFalseTest(self, input_path, text):
        with input_path.open() as json_file:
            input_data = json.load(json_file)
        self.assertFalse(self.udv.validate(input_data), text)

    def testValidatorNoUserId(self):
        path = self.base_path / 'user_data_no_user_id.json'
        self.__doFalseTest(path, "No user id provided")

    def testValidatorEmptyData(self):
        path = self.base_path / 'user_data_empty_data.json'
        self.__doTrueTest(path, "No data provided")

    def testValidatorEmptyListsOfData(self):
        path = self.base_path / 'user_data_empty_lists_of_data.json'
        self.__doTrueTest(path, "Lists of empty data provided")

    def testValidatorFullData(self):
        path = self.base_path / 'user_data_full_data.json'
        self.__doTrueTest(path, "Full data provided")

    def testValidatorOneData(self):
        path = self.base_path / 'user_data_one_data.json'
        self.__doTrueTest(path, "One data provided")

    def testValidatorWrongFirstLevel(self):
        path = self.base_path / 'user_data_wrong_first_level.json'
        self.__doFalseTest(path, "Wrong data provided at first level")

    def testValidatorWrongSecondLevel(self):
        path = self.base_path / 'user_data_wrong_second_level.json'
        self.__doFalseTest(path, "Wrong data provided at second level")

    def testValidatorWrongThirdLevelLeave(self):
        path = self.base_path / 'user_data_wrong_third_level_leave.json'
        self.__doFalseTest(path, "Wrong data provided at third level")

    def testValidatorWrongThirdLevelNonLeave(self):
        path = self.base_path / 'user_data_wrong_third_level_non_leave.json'
        self.__doFalseTest(path, "Wrong data provided at third level")

    def testValidatorWrongFourthLevel(self):
        path = self.base_path / 'user_data_wrong_fourth_level.json'
        self.__doFalseTest(path, "Wrong data provided at fourth level")


if __name__ == '__main__':
    unittest.main()
