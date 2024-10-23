from flask import Blueprint, jsonify, request
from authentification import check_credentials

personalshot_bp = Blueprint('personalshot_bp', __name__)

@personalshot_bp.before_request
def before_request():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not check_credentials(auth_header):
        return jsonify({"message": "Unauthorized"}), 401

@personalshot_bp.route('/personalshot/action1', methods=['GET'])
def personalshot_action1():
    return jsonify({"message": "Personalshot Action 1"}), 200

@personalshot_bp.route('/personalshot/action2', methods=['POST'])
def personalshot_action2():
    data = request.get_json()
    return jsonify({"message": "Personalshot Action 2", "data": data}), 200
