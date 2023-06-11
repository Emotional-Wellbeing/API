import json
import unittest
from pathlib import Path

from flask import Flask

from endpoints import Endpoints


class TestUserDataValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.endpoints = Endpoints()
        self.app = Flask(__name__)
        self.base_path_input = Path(__file__).parent / '../json/input'
        self.base_path_response = Path(__file__).parent / '../json/response'
        self.bad_response_bytes = "Bad request".encode("UTF-8")

    def __doSuccessTest(self, input_path, response_path):
        with input_path.open() as json_file:
            input_data = json.load(json_file)
        with response_path.open() as json_file:
            response_data = json.load(json_file)

        with self.app.app_context():
            response = self.endpoints.user_data_endpoint(input_data)

        self.assertEqual(response.status_code, 200, "Response must be OK")
        self.assertDictEqual(response.json, response_data, "Content must be equal")

    def __doFailureTest(self, input_path):
        with input_path.open() as json_file:
            input_data = json.load(json_file)

        with self.app.app_context():
            response = self.endpoints.user_data_endpoint(input_data)

        self.assertEqual(response.status_code, 400, "Code must be 400: bad request")
        self.assertIsNone(response.json, "Response json must be None")
        self.assertEqual(response.data, self.bad_response_bytes, "Data of the response is \"Bad response\" as bytes")

    def testValidatorNoUserId(self):
        input_path = self.base_path_input / 'user_data_no_user_id.json'
        self.__doFailureTest(input_path)

    def testValidatorEmptyData(self):
        input_path = self.base_path_input / 'user_data_empty_data.json'
        response_path = self.base_path_response / 'user_data_empty_data.json'

        self.__doSuccessTest(input_path, response_path)

    def testValidatorFullData(self):
        input_path = self.base_path_input / 'user_data_full_data.json'
        response_path = self.base_path_response / 'user_data_full_data.json'

        self.__doSuccessTest(input_path, response_path)

    def testValidatorOneData(self):
        input_path = self.base_path_input / 'user_data_one_data.json'
        response_path = self.base_path_response / 'user_data_one_data.json'

        self.__doSuccessTest(input_path, response_path)

    def testValidatorWrongFirstLevel(self):
        input_path = self.base_path_input / 'user_data_wrong_first_level.json'
        self.__doFailureTest(input_path)

    def testValidatorWrongSecondLevel(self):
        input_path = self.base_path_input / 'user_data_wrong_second_level.json'
        self.__doFailureTest(input_path)

    def testValidatorWrongThirdLevelLeave(self):
        input_path = self.base_path_input / 'user_data_wrong_third_level_leave.json'
        self.__doFailureTest(input_path)

    def testValidatorWrongThirdLevelNonLeave(self):
        input_path = self.base_path_input / 'user_data_wrong_third_level_non_leave.json'
        self.__doFailureTest(input_path)

    def testValidatorWrongFourthLevel(self):
        input_path = self.base_path_input / 'user_data_wrong_fourth_level.json'
        self.__doFailureTest(input_path)


if __name__ == '__main__':
    unittest.main()
