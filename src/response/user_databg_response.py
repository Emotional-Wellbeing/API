from typing import Dict
from src.utils import data_not_empty


def build_user_databg_response(user_databg: Dict) -> Dict:
    """
    Build user background data response, returning for each measure the max timestamp received
    :param user_databg:
    :return: Dict with measures as keys and timestamps as values
    """
    response = {}

    if data_not_empty(user_databg):
        for measure, values in user_databg.items():
            timestamps = []
            for register in values:
                for key in register:
                    if key in ("WiFI", "Mobile", "Call", "App"):
                        timestamps.append(measure[key])
            if len(timestamps) > 0:
                response[measure] = max(timestamps)
    return response
