from typing import Dict

from flask import Response, jsonify

from database import Database
from response.user_data_response import build_user_data_response
from response.user_databg_response import build_user_databg_response
from utils import data_not_empty
from validator.user_data_validator import UserDataValidator
from validator.user_databg_validator import UserDataBgValidator 
from utils import obtain_logger

logger = obtain_logger("API")


class Endpoints:
    def __init__(self):
        self.udv = UserDataValidator()
        self.udbgv = UserDataBgValidator()
        self.database = Database()

    def user_data_endpoint(self, request_data: Dict) -> Response:
        if self.udv.validate(request_data):
            if data_not_empty(request_data["data"]):
                self.database.insert_user_data(request_data)
            response = build_user_data_response(request_data["data"])
            return jsonify(response)
        else:
            return Response("Bad request", 400)
    
    def user_databg_endpoint(self, request_databg: Dict) -> Response:
        if self.udbgv.validate(request_databg):
            if data_not_empty(request_databg):
                logger.info(f'data_not_empty')
                self.database.insert_user_databg(request_databg)
                logger.info(f'insert_user_databg')
                response = build_user_databg_response(request_databg)
                logger.info(f'build_user_databg_response')
                return jsonify(response)
        else:
            return Response("Bad request", 400)
