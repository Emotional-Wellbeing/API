import json

from flask import Flask, jsonify, request, Response
from random import randint

# Init
app = Flask(__name__)


@app.route('/score')
def score():
    """Returns the score of the community"""
    return jsonify(randint(0, 100))


@app.route('/user_data', methods=["POST"])
def user_data():
    """Save user data from the app"""
    request_data = request.get_json()
    json_formatted_str = json.dumps(request_data, indent=2)
    print(json_formatted_str)

    return Response("success", 200)


@app.route('/questionnaire_data', methods=["POST"])
def questionnaire_data():
    """Save user questionnaires data from the app"""
    request_data = request.get_json()
    print(request_data)
    return Response("success", 200)


# If this script is being executed and not imported, deploy the API
if __name__ == '__main__':
    app.run(host="0.0.0.0")
