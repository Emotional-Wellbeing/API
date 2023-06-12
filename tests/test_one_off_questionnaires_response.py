import json
import unittest
from pathlib import Path

from src.response.one_off_questionnaires_response import build_one_off_questionnaires_response


class TestOneOffQuestionnairesResponse(unittest.TestCase):
    def setUp(self) -> None:
        self.base_path_input = Path(__file__).parent / '../json/input'
        self.base_path_response = Path(__file__).parent / '../json/response'

    def __doTest(self, input_path, response_path, text):
        with input_path.open() as json_file:
            input_data = json.load(json_file)
        with response_path.open() as json_file:
            expected_response = json.load(json_file)

        response = build_one_off_questionnaires_response(input_data["data"])
        self.assertDictEqual(response, expected_response, text)

    def testResponseEmptyData(self):
        input_path = self.base_path_input / 'one_off_questionnaires_empty_data.json'
        response_path = self.base_path_response / 'one_off_questionnaires_empty_data.json'

        self.__doTest(input_path, response_path, "No data provided")

    def testResponseEmptyListsOfData(self):
        input_path = self.base_path_input / 'one_off_questionnaires_empty_lists_of_data.json'
        response_path = self.base_path_response / 'one_off_questionnaires_empty_lists_of_data.json'

        self.__doTest(input_path, response_path, "Lists of empty data provided")

    def testResponseFullData(self):
        input_path = self.base_path_input / 'one_off_questionnaires_full_data.json'
        response_path = self.base_path_response / 'one_off_questionnaires_full_data.json'

        self.__doTest(input_path, response_path, "Full data provided")

    def testResponseOneData(self):
        input_path = self.base_path_input / 'one_off_questionnaires_one_data.json'
        response_path = self.base_path_response / 'one_off_questionnaires_one_data.json'

        self.__doTest(input_path, response_path, "One data provided")


if __name__ == '__main__':
    unittest.main()
