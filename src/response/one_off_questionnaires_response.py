from typing import Dict

from src.utils import data_not_empty


def build_one_off_questionnaires_response(user_data: Dict) -> Dict:
    """
    Build one_off questionnaires response, returning for each measure the max timestamp received
    :param user_data: Dictionary with measures as keys
    :return: Dict with measures as keys and timestamps as values
    """
    response = {}
    if data_not_empty(user_data):
        for measure, values in user_data.items():
            timestamps = []
            for register in values:
                for key in register:
                    if key == "modifiedAt":
                        timestamps.append(register[key])
            if len(timestamps) > 0:
                response[measure] = max(timestamps)
    return response
