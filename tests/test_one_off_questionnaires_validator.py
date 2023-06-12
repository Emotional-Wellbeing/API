import json
import unittest
from pathlib import Path

from src.validator.one_off_questionnaires_validator import OneOffQuestionnairesValidator


class TestOneOffQuestionnairesValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.ooqv = OneOffQuestionnairesValidator()
        self.base_path = Path(__file__).parent / '../json/input'

    def __doTrueTest(self, input_path, text):
        with input_path.open() as json_file:
            input_data = json.load(json_file)
        self.assertTrue(self.ooqv.validate(input_data), text)

    def __doFalseTest(self, input_path, text):
        with input_path.open() as json_file:
            input_data = json.load(json_file)
        self.assertFalse(self.ooqv.validate(input_data), text)

    def testValidatorNoUserId(self):
        path = self.base_path / 'one_off_questionnaires_no_user_id.json'
        self.__doFalseTest(path, "No user id provided")

    def testValidatorEmptyData(self):
        path = self.base_path / 'one_off_questionnaires_empty_data.json'
        self.__doTrueTest(path, "No data provided")

    def testValidatorEmptyListsOfData(self):
        path = self.base_path / 'one_off_questionnaires_empty_lists_of_data.json'
        self.__doTrueTest(path, "Lists of empty data provided")

    def testValidatorFullData(self):
        path = self.base_path / 'one_off_questionnaires_full_data.json'
        self.__doTrueTest(path, "Full data provided")

    def testValidatorOneData(self):
        path = self.base_path / 'one_off_questionnaires_one_data.json'
        self.__doTrueTest(path, "One data provided")

    def testValidatorWrongFirstLevel(self):
        path = self.base_path / 'one_off_questionnaires_wrong_first_level.json'
        self.__doFalseTest(path, "Wrong data provided at first level")

    def testValidatorWrongSecondLevel(self):
        path = self.base_path / 'one_off_questionnaires_wrong_second_level.json'
        self.__doFalseTest(path, "Wrong data provided at second level")

    def testValidatorWrongThirdLevel(self):
        path = self.base_path / 'one_off_questionnaires_wrong_third_level.json'
        self.__doFalseTest(path, "Wrong data provided at third level")


if __name__ == '__main__':
    unittest.main()
