import json
from flask import jsonify


def get_json_result(state, data, message):
    json_data = {'state': state, 'message': message, 'data': data}
    return json_data
