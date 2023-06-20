import json
from pathlib import Path
from typing import Dict


class UserDataBgValidator:
    def __init__(self):
        # If we use this class from other script that is allocated on other folder and we don't user __file__,
        # Python won't recognise the path.
        request_format_path = Path(__file__).parent / "user_databg_request_format.json"
        with request_format_path.open() as request_format_file:
            request_format_raw = json.load(request_format_file)
            self.request_format = request_format_raw.keys()
            self.data_format = request_format_raw["databg"]

    def validate(self, user_databg_request: Dict) -> bool:
        """
            Checks if whole user_databg_request is correct at syntax level
            :param user_databg_request: Request parsed in dict format
            :return: true if user_data_request is correct, otherwise false
        """
        result = self.__validate_request_format(user_databg_request)
        return result

    def __validate_request_format(self, user_databg_request: Dict) -> bool:
        """
            Checks if user_databg_request is correct at syntax level (userId and data)
            :param user_databg_request: Request parsed in dict format
            :return: true if user_databg_request is correct, otherwise false
        """
        result = True
        for field in self.request_format:
            if field not in user_databg_request:
                result = False
        return result
