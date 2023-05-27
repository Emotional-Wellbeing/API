from random import randint

from flask import Flask, jsonify, request, Response

from src.endpoints import Endpoints
from src.utils import obtain_logger

# Init
app = Flask(__name__)
endpoints = Endpoints()
logger = obtain_logger("API")


@app.route('/score')
def score():
    """Returns the score of the community"""
    return jsonify(randint(0, 100))


@app.route('/user_data', methods=["POST"])
def user_data():
    """Save user data from the app"""
    request_data = request.json
    logger.info(f'A request has been received with the following data: {request_data}')
    return endpoints.user_data_endpoint(request_data)


@app.route('/questionnaire_data', methods=["POST"])
def questionnaire_data():
    """Save user questionnaires data from the app"""
    return Response("success", 200)


# If this script is being executed and not imported, deploy the API
if __name__ == '__main__':
    app.run(host="0.0.0.0")
