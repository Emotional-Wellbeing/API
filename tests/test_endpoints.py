import json
import unittest
from pathlib import Path

from flask import Flask

from src.endpoints import Endpoints


class TestUserDataValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.endpoints = Endpoints()
        self.app = Flask(__name__)
        self.base_path_input = Path(__file__).parent / '../json/input'
        self.base_path_response = Path(__file__).parent / '../json/response'
        self.bad_response_bytes = "Bad request".encode("UTF-8")

    def __doSuccessUserDataTest(self, input_path, response_path):
        with input_path.open() as json_file:
            input_data = json.load(json_file)
        with response_path.open() as json_file:
            response_data = json.load(json_file)

        with self.app.app_context():
            response = self.endpoints.user_data_endpoint(input_data)

        self.assertEqual(response.status_code, 200, "Response must be OK")
        self.assertDictEqual(response.json, response_data, "Content must be equal")

    def __doFailureUserDataTest(self, input_path):
        with input_path.open() as json_file:
            input_data = json.load(json_file)

        with self.app.app_context():
            response = self.endpoints.user_data_endpoint(input_data)

        self.assertEqual(response.status_code, 400, "Code must be 400: bad request")
        self.assertIsNone(response.json, "Response json must be None")
        self.assertEqual(response.data, self.bad_response_bytes, "Data of the response is \"Bad response\" as bytes")

    def __doSuccessDailyQuestionnairesTest(self, input_path, response_path):
        with input_path.open() as json_file:
            input_data = json.load(json_file)
        with response_path.open() as json_file:
            response_data = json.load(json_file)

        with self.app.app_context():
            response = self.endpoints.daily_questionnaires_endpoint(input_data)

        self.assertEqual(response.status_code, 200, "Response must be OK")
        self.assertDictEqual(response.json, response_data, "Content must be equal")

    def __doFailureDailyQuestionnairesTest(self, input_path):
        with input_path.open() as json_file:
            input_data = json.load(json_file)

        with self.app.app_context():
            response = self.endpoints.daily_questionnaires_endpoint(input_data)

        self.assertEqual(response.status_code, 400, "Code must be 400: bad request")
        self.assertIsNone(response.json, "Response json must be None")
        self.assertEqual(response.data, self.bad_response_bytes, "Data of the response is \"Bad response\" as bytes")

    def testUserDataValidatorNoUserId(self):
        input_path = self.base_path_input / 'user_data_no_user_id.json'
        self.__doFailureUserDataTest(input_path)

    def testUserDataValidatorEmptyData(self):
        input_path = self.base_path_input / 'user_data_empty_data.json'
        response_path = self.base_path_response / 'user_data_empty_data.json'

        self.__doSuccessUserDataTest(input_path, response_path)

    def testUserDataValidatorFullData(self):
        input_path = self.base_path_input / 'user_data_full_data.json'
        response_path = self.base_path_response / 'user_data_full_data.json'

        self.__doSuccessUserDataTest(input_path, response_path)

    def testUserDataValidatorOneData(self):
        input_path = self.base_path_input / 'user_data_one_data.json'
        response_path = self.base_path_response / 'user_data_one_data.json'

        self.__doSuccessUserDataTest(input_path, response_path)

    def testUserDataValidatorWrongFirstLevel(self):
        input_path = self.base_path_input / 'user_data_wrong_first_level.json'
        self.__doFailureUserDataTest(input_path)

    def testUserDataValidatorWrongSecondLevel(self):
        input_path = self.base_path_input / 'user_data_wrong_second_level.json'
        self.__doFailureUserDataTest(input_path)

    def testUserDataValidatorWrongThirdLevelLeave(self):
        input_path = self.base_path_input / 'user_data_wrong_third_level_leave.json'
        self.__doFailureUserDataTest(input_path)

    def testUserDataValidatorWrongThirdLevelNonLeave(self):
        input_path = self.base_path_input / 'user_data_wrong_third_level_non_leave.json'
        self.__doFailureUserDataTest(input_path)

    def testUserDataValidatorWrongFourthLevel(self):
        input_path = self.base_path_input / 'user_data_wrong_fourth_level.json'
        self.__doFailureUserDataTest(input_path)

    def testDailyQuestionnairesNoUserId(self):
        input_path = self.base_path_input / 'daily_questionnaires_no_user_id.json'
        self.__doFailureDailyQuestionnairesTest(input_path)

    def testDailyQuestionnairesEmptyData(self):
        input_path = self.base_path_input / 'daily_questionnaires_empty_data.json'
        response_path = self.base_path_response / 'daily_questionnaires_empty_data.json'

        self.__doSuccessDailyQuestionnairesTest(input_path, response_path)

    def testDailyQuestionnairesEmptyListsOfData(self):
        input_path = self.base_path_input / 'daily_questionnaires_empty_lists_of_data.json'
        response_path = self.base_path_response / 'daily_questionnaires_empty_lists_of_data.json'

        self.__doSuccessDailyQuestionnairesTest(input_path, response_path)

    def testDailyQuestionnairesFullData(self):
        input_path = self.base_path_input / 'daily_questionnaires_full_data.json'
        response_path = self.base_path_response / 'daily_questionnaires_full_data.json'

        self.__doSuccessDailyQuestionnairesTest(input_path, response_path)

    def testDailyQuestionnairesOneData(self):
        input_path = self.base_path_input / 'daily_questionnaires_one_data.json'
        response_path = self.base_path_response / 'daily_questionnaires_one_data.json'

        self.__doSuccessDailyQuestionnairesTest(input_path, response_path)

    def testDailyQuestionnairesWrongFirstLevel(self):
        input_path = self.base_path_input / 'daily_questionnaires_wrong_first_level.json'
        self.__doFailureDailyQuestionnairesTest(input_path)

    def testDailyQuestionnairesWrongSecondLevel(self):
        input_path = self.base_path_input / 'daily_questionnaires_wrong_second_level.json'
        self.__doFailureDailyQuestionnairesTest(input_path)

    def testDailyQuestionnairesWrongThirdLevel(self):
        input_path = self.base_path_input / 'daily_questionnaires_wrong_third_level.json'
        self.__doFailureDailyQuestionnairesTest(input_path)


if __name__ == '__main__':
    unittest.main()
