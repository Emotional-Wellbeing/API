import json
from pathlib import Path
from typing import Dict

from src.utils.utils import inner_contained_fully_outer


class UserDataValidator:
    def __init__(self):
        # If we use this class from other script that is allocated on other folder and we don't user __file__,
        # Python won't recognise the path.
        request_format_path = Path(__file__).parent / "user_data_request_format.json"
        with request_format_path.open() as request_format_file:
            request_format_raw = json.load(request_format_file)
            self.request_format = request_format_raw.keys()
            self.data_format = request_format_raw["data"]

    def validate(self, user_data_request: Dict) -> bool:
        """
            Checks if whole user_data_request is correct at syntax level
            :param user_data_request: Request parsed in dict format
            :return: true if user_data_request is correct, otherwise false
        """
        result = self.__validate_request_format(user_data_request)
        if result:
            result = self.__validate_user_data_format(user_data_request["data"])
        return result

    def __validate_request_format(self, user_data_request: Dict) -> bool:
        """
            Checks if user_data_request is correct at syntax level (userId and data)
            :param user_data_request: Request parsed in dict format
            :return: true if user_data_request is correct, otherwise false
        """
        result = True
        for field in self.request_format:
            if field not in user_data_request:
                result = False
        return result

    def __validate_user_data_format(self, user_data: Dict) -> bool:
        """
            Checks if user_data is correct at syntax level (measures in all nested levels)
            :param user_data: User data of the request
            :return: true if user_data is correct, otherwise false
        """
        result = True
        # Iter over all measures of the data. All of them must match any available field
        for measure, values in user_data.items():
            if measure in self.data_format.keys():
                # Check second level, these are mandatory
                for register in values:
                    # If there isn't third level, only check current level
                    if type(self.data_format[measure]) is list:
                        if not inner_contained_fully_outer(self.data_format[measure], register.keys()):
                            result = False
                    # If there is third level, check current level and later check third level
                    elif type(self.data_format[measure]) is dict:
                        if inner_contained_fully_outer(self.data_format[measure].keys(), register.keys()):
                            # Check third level
                            for key, value in self.data_format[measure].items():
                                # Not all of second level contains child elements, so check if we have children
                                if type(value) is list:
                                    for innerRegister in register[key]:
                                        if not inner_contained_fully_outer(self.data_format[measure][key],
                                                                           innerRegister.keys()):
                                            result = False
                        else:
                            result = False
            else:
                result = False
        return result
