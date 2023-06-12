from typing import Dict

from flask import Response, jsonify

from src.database import Database
from src.response.daily_questionnaires_response import build_daily_questionnaires_response
from src.response.one_off_questionnaires_response import build_one_off_questionnaires_response
from src.response.user_data_response import build_user_data_response
from src.utils import data_not_empty
from src.validator.daily_questionnaires_validator import DailyQuestionnairesValidator
from src.validator.one_off_questionnaires_validator import OneOffQuestionnairesValidator
from src.validator.user_data_validator import UserDataValidator


class Endpoints:
    def __init__(self):
        self.udv = UserDataValidator()
        self.dqv = DailyQuestionnairesValidator()
        self.ooqv = OneOffQuestionnairesValidator()
        self.database = Database()

    def user_data_endpoint(self, request_data: Dict) -> Response:
        if self.udv.validate(request_data):
            if data_not_empty(request_data["data"]):
                self.database.insert_user_data(request_data)
            response = build_user_data_response(request_data["data"])
            return jsonify(response)
        else:
            return Response("Bad request", 400)

    def daily_questionnaires_endpoint(self, request_data: Dict) -> Response:
        if self.dqv.validate(request_data):
            if data_not_empty(request_data["data"]):
                self.database.insert_daily_questionnaires(request_data)
            response = build_daily_questionnaires_response(request_data["data"])
            return jsonify(response)
        else:
            return Response("Bad request", 400)

    def one_off_questionnaires_endpoint(self, request_data: Dict) -> Response:
        if self.ooqv.validate(request_data):
            if data_not_empty(request_data["data"]):
                self.database.insert_one_off_questionnaires(request_data)
            response = build_one_off_questionnaires_response(request_data["data"])
            return jsonify(response)
        else:
            return Response("Bad request", 400)
