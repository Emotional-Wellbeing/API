import json

import unittest

from src.validator.user_data_validator import UserDataValidator


class TestUserDataValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.udv = UserDataValidator()

    def test_validator_no_user_id(self):
        with open('../json/user_data_no_user_id.json') as json_file:
            data = json.load(json_file)
        self.assertFalse(self.udv.validate(data), "No user id provided")

    def test_validator_empty_data(self):
        with open('../json/user_data_empty_data.json') as json_file:
            data = json.load(json_file)
        self.assertTrue(self.udv.validate(data), "No data provided")

    def test_validator_full_data(self):
        with open('../json/user_data_full_data.json') as json_file:
            data = json.load(json_file)
        self.assertTrue(self.udv.validate(data), "Full data provided")

    def test_validator_one_data(self):
        with open('../json/user_data_one_data.json') as json_file:
            data = json.load(json_file)
        self.assertTrue(self.udv.validate(data), "One data provided")

    def test_validator_wrong_first_level(self):
        with open('../json/user_data_wrong_first_level.json') as json_file:
            data = json.load(json_file)
        self.assertFalse(self.udv.validate(data), "Wrong data provided at first level")

    def test_validator_wrong_second_level(self):
        with open('../json/user_data_wrong_second_level.json') as json_file:
            data = json.load(json_file)
        self.assertFalse(self.udv.validate(data), "Wrong data provided at second level")

    def test_validator_wrong_third_level(self):
        with open('../json/user_data_wrong_third_level.json') as json_file:
            data = json.load(json_file)
        self.assertFalse(self.udv.validate(data), "Wrong data provided at third level")

    def test_validator_wrong_fourth_level(self):
        with open('../json/user_data_wrong_fourth_level.json') as json_file:
            data = json.load(json_file)
        self.assertFalse(self.udv.validate(data), "Wrong data provided at fourth level")


if __name__ == '__main__':
    unittest.main()
