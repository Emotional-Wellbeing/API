import json
import unittest
from pathlib import Path

from flask import Flask

from src.endpoints import Endpoints


class TestOneOffQuestionnairesEndpoint(unittest.TestCase):
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
            response = self.endpoints.one_off_questionnaires_endpoint(input_data)

        self.assertEqual(response.status_code, 200, "Response must be OK")
        self.assertDictEqual(response.json, response_data, "Content must be equal")

    def __doFailureTest(self, input_path):
        with input_path.open() as json_file:
            input_data = json.load(json_file)

        with self.app.app_context():
            response = self.endpoints.one_off_questionnaires_endpoint(input_data)

        self.assertEqual(response.status_code, 400, "Code must be 400: bad request")
        self.assertIsNone(response.json, "Response json must be None")
        self.assertEqual(response.data, self.bad_response_bytes, "Data of the response is \"Bad response\" as bytes")

    def testNoUserId(self):
        input_path = self.base_path_input / 'one_off_questionnaires_no_user_id.json'
        self.__doFailureTest(input_path)

    def testEmptyData(self):
        input_path = self.base_path_input / 'one_off_questionnaires_empty_data.json'
        response_path = self.base_path_response / 'one_off_questionnaires_empty_data.json'

        self.__doSuccessTest(input_path, response_path)

    def testEmptyListsOfData(self):
        input_path = self.base_path_input / 'one_off_questionnaires_empty_lists_of_data.json'
        response_path = self.base_path_response / 'one_off_questionnaires_empty_lists_of_data.json'

        self.__doSuccessTest(input_path, response_path)

    def testFullData(self):
        input_path = self.base_path_input / 'one_off_questionnaires_full_data.json'
        response_path = self.base_path_response / 'one_off_questionnaires_full_data.json'

        self.__doSuccessTest(input_path, response_path)

    def testOneData(self):
        input_path = self.base_path_input / 'one_off_questionnaires_one_data.json'
        response_path = self.base_path_response / 'one_off_questionnaires_one_data.json'

        self.__doSuccessTest(input_path, response_path)

    def testWrongFirstLevel(self):
        input_path = self.base_path_input / 'one_off_questionnaires_wrong_first_level.json'
        self.__doFailureTest(input_path)

    def testWrongSecondLevel(self):
        input_path = self.base_path_input / 'one_off_questionnaires_wrong_second_level.json'
        self.__doFailureTest(input_path)

    def testWrongThirdLevel(self):
        input_path = self.base_path_input / 'one_off_questionnaires_wrong_third_level.json'
        self.__doFailureTest(input_path)


if __name__ == '__main__':
    unittest.main()
