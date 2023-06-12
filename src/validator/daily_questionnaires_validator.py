import json
from pathlib import Path
from typing import Dict

from src.utils import inner_contained_fully_outer


class DailyQuestionnairesValidator:
    def __init__(self):
        # If we use this class from other script that is allocated on other folder and we don't user __file__,
        # Python won't recognise the path.
        request_format_path = Path(__file__).parent / "daily_questionnaires_request_format.json"
        with request_format_path.open() as request_format_file:
            request_format_raw = json.load(request_format_file)
            self.request_format = request_format_raw.keys()
            self.data_format = request_format_raw["data"]

    def validate(self, daily_questionnaires_request: Dict) -> bool:
        """
            Checks if whole daily_questionnaires_request is correct at syntax level
            :param daily_questionnaires_request: Request parsed in dict format
            :return: true if daily_questionnaires_request is correct, otherwise false
        """
        result = self.__validate_request_format(daily_questionnaires_request)
        if result:
            result = self.__validate_daily_questionnaires_format(daily_questionnaires_request["data"])
        return result

    def __validate_request_format(self, daily_questionnaires_request: Dict) -> bool:
        """
            Checks if daily_questionnaires_request is correct at syntax level (userId and data)
            :param daily_questionnaires_request: Request parsed in dict format
            :return: true if daily_questionnaires_request is correct, otherwise false
        """
        result = True
        for field in self.request_format:
            if field not in daily_questionnaires_request:
                result = False
        return result

    def __validate_daily_questionnaires_format(self, daily_questionnaires: Dict) -> bool:
        """
            Checks if daily_questionnaires is correct at syntax level (measures in all nested levels)
            :param daily_questionnaires: User data of the request
            :return: true if daily_questionnaires is correct, otherwise false
        """
        result = True
        # Iter over all measures of the data. All of them must match any available field
        for measure, values in daily_questionnaires.items():
            if measure in self.data_format.keys():
                # Check second level, these are mandatory
                for register in values:
                    if not inner_contained_fully_outer(self.data_format[measure], register.keys()):
                        result = False
            else:
                result = False
        return result
