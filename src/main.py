from flask import Flask, jsonify, request, Response
from random import randint

from src.response.process import build_user_data_response
from src.validator.user_data_validator import UserDataValidator

# Init
app = Flask(__name__)
usv = UserDataValidator()


@app.route('/score')
def score():
    """Returns the score of the community"""
    return jsonify(randint(0, 100))


@app.route('/user_data', methods=["POST"])
def user_data():
    """Save user data from the app"""
    request_data = request.json
    if usv.validate(request_data):
        response = build_user_data_response(request_data["data"])
        return jsonify(response)
    else:
        return Response("Bad request", 400)


@app.route('/questionnaire_data', methods=["POST"])
def questionnaire_data():
    """Save user questionnaires data from the app"""
    request_data = request.get_json()
    return Response("success", 200)


# If this script is being executed and not imported, deploy the API
if __name__ == '__main__':
    app.run(host="0.0.0.0")
