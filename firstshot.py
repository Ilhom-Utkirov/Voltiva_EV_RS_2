from flask import Blueprint, jsonify, request
from authentification import check_credentials

firstshot_bp = Blueprint('firstshot_bp', __name__)

@firstshot_bp.before_request
def before_request():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not check_credentials(auth_header):
        return jsonify({"message": "Unauthorized"}), 401

@firstshot_bp.route('/firstshot/action1', methods=['GET'])
def firstshot_action1():
    return jsonify({"message": "Firstshot Action 1"}), 200

@firstshot_bp.route('/firstshot/action2', methods=['POST'])
def firstshot_action2():
    data = request.get_json()
    return jsonify({"message": "Firstshot Action 2", "data": data}), 200
