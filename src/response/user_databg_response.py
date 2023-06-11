from typing import Dict
from utils import data_not_empty

from utils import obtain_logger

logger = obtain_logger("API")


def build_user_databg_response(user_databg: Dict) -> Dict:
    """
    Build user background data response, returning for each measure the max timestamp received
    :param user_data: Dictionary with measures as keys
    :return: Dict with measures as keys and timestamps as values
    """
    response = {}

    if data_not_empty(user_databg):
        for measure, values in user_databg.items():
            timestamps = []
            for register in values:                
                for key in register:
                    #if key in ("WiFI", "Mobile"):
                    timestamps.append(register[key])
            if len(timestamps) > 0:
                response[measure] = max(timestamps)
    return response
