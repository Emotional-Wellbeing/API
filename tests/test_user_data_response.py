import json
import unittest
from pathlib import Path

from src.response.user_data_response import build_user_data_response


class TestUserDataValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.base_path_input = Path(__file__).parent / '../json/input'
        self.base_path_response = Path(__file__).parent / '../json/response'

    def __doTest(self, input_path, response_path, text):
        with input_path.open() as json_file:
            input_data = json.load(json_file)
        with response_path.open() as json_file:
            expected_response = json.load(json_file)

        response = build_user_data_response(input_data["data"])
        self.assertDictEqual(response, expected_response, text)

    def testValidatorEmptyData(self):
        input_path = self.base_path_input / 'user_data_empty_data.json'
        response_path = self.base_path_response / 'user_data_empty_data.json'

        self.__doTest(input_path, response_path, "No data provided")

    def testValidatorFullData(self):
        input_path = self.base_path_input / 'user_data_full_data.json'
        response_path = self.base_path_response / 'user_data_full_data.json'

        self.__doTest(input_path, response_path, "Full data provided")

    def testValidatorOneData(self):
        input_path = self.base_path_input / 'user_data_one_data.json'
        response_path = self.base_path_response / 'user_data_one_data.json'

        self.__doTest(input_path, response_path, "One data provided")


if __name__ == '__main__':
    unittest.main()
