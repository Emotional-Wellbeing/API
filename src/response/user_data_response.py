from typing import Dict


def build_user_data_response(user_data: Dict) -> Dict:
    """
    Build user data response, returning for each measure the max timestamp received
    :param user_data: Dictionary with measures as keys
    :return: Dict with measures as keys and timestamps as values
    """
    response = {}
    for measure, values in user_data.items():
        timestamps = []
        for register in values:
            for key in register:
                if key in ("endTime", "timestamp"):
                    timestamps.append(register[key])
        response[measure] = max(timestamps)
    return response
