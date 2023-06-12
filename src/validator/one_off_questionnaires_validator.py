import json
from pathlib import Path
from typing import Dict

from src.utils import inner_contained_fully_outer


class OneOffQuestionnairesValidator:
    def __init__(self):
        # If we use this class from other script that is allocated on other folder and we don't user __file__,
        # Python won't recognise the path.
        request_format_path = Path(__file__).parent / "one_off_questionnaires_request_format.json"
        with request_format_path.open() as request_format_file:
            request_format_raw = json.load(request_format_file)
            self.request_format = request_format_raw.keys()
            self.data_format = request_format_raw["data"]

    def validate(self, one_off_questionnaires_request: Dict) -> bool:
        """
            Checks if whole one_off_questionnaires_request is correct at syntax level
            :param one_off_questionnaires_request: Request parsed in dict format
            :return: true if one_off_questionnaires_request is correct, otherwise false
        """
        result = self.__validate_request_format(one_off_questionnaires_request)
        if result:
            result = self.__validate_one_off_questionnaires_format(one_off_questionnaires_request["data"])
        return result

    def __validate_request_format(self, one_off_questionnaires_request: Dict) -> bool:
        """
            Checks if one_off_questionnaires_request is correct at syntax level (userId and data)
            :param one_off_questionnaires_request: Request parsed in dict format
            :return: true if one_off_questionnaires_request is correct, otherwise false
        """
        result = True
        for field in self.request_format:
            if field not in one_off_questionnaires_request:
                result = False
        return result

    def __validate_one_off_questionnaires_format(self, one_off_questionnaires: Dict) -> bool:
        """
            Checks if one_off_questionnaires is correct at syntax level (measures in all nested levels)
            :param one_off_questionnaires: User data of the request
            :return: true if one_off_questionnaires is correct, otherwise false
        """
        result = True
        # Iter over all measures of the data. All of them must match any available field
        for measure, values in one_off_questionnaires.items():
            if measure in self.data_format.keys():
                # Check second level, these are mandatory
                for register in values:
                    if not inner_contained_fully_outer(self.data_format[measure], register.keys()):
                        result = False
            else:
                result = False
        return result
