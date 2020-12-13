from config import *
from repository.models import *
from services.user_service import add_user, get_user
from exceptions.errors import *
import json
import re

@app.route('/user', methods=['POST'])
def create_user():
    if not request.is_json:
        return jsonify({"message": "Body is required"}), 400

    user = None

    try:
        user = add_user(request)
    except ValueError as err:
        return jsonify({"message": str(err)}), 400
    except ItemAlreadyExistsError as err:
        return jsonify({"messgae": str(err)}), 409

    return jsonify(user), 201

@app.route('/user/provisor', methods=['POST'])
def create_user_provisor():
    if not request.is_json:
        return jsonify({"message": "Body is required"}), 400

    user = None

    try:
        user = add_user(request, role='provisor')
    except ValueError as err:
        return jsonify({"message": str(err)}), 400
    except ItemAlreadyExistsError as err:
        return jsonify({"messgae": str(err)}), 409

    return jsonify(user), 201

@app.route('/user/<user_id>', methods=['GET'])
def get_user_by_id(user_id):

    regex = re.compile('[\w]{8}(-[\w]{4}){3}-[\w]{12}\Z')
    is_correct_id = regex.match(user_id)

    if not is_correct_id:
        return jsonify({'message': 'Invalid id provided' }), 400
    
    try:
        user = get_user(user_id)

        return jsonify(user), 200
    except NotFoundError as err:
        return jsonify({"message": str(err)}), 404