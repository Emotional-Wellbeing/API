from typing import Dict

from flask import Response, jsonify

from src.response.user_data_response import build_user_data_response
from src.validator.user_data_validator import UserDataValidator


class Endpoints:
    def __init__(self):
        self.udv = UserDataValidator()

    def user_data_endpoint(self, request_data: Dict) -> Response:
        if self.udv.validate(request_data):
            response = build_user_data_response(request_data["data"])
            return jsonify(response)
        else:
            return Response("Bad request", 400)
