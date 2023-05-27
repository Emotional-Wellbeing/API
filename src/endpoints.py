from typing import Dict

from flask import Response, jsonify

from src.database import Database
from src.response.user_data_response import build_user_data_response
from src.utils import data_not_empty
from src.validator.user_data_validator import UserDataValidator


class Endpoints:
    def __init__(self):
        self.udv = UserDataValidator()
        self.database = Database()

    def user_data_endpoint(self, request_data: Dict) -> Response:
        if self.udv.validate(request_data):
            if data_not_empty(request_data["data"]):
                self.database.insert_user_data(request_data)
            response = build_user_data_response(request_data["data"])
            return jsonify(response)
        else:
            return Response("Bad request", 400)
