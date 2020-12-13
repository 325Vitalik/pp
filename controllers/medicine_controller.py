from config import *
from repository.models import *
from services.medicine_service import *
from exceptions.errors import *
import json
import re

@app.route('/medicine', methods=['POST'])
def create_medicine():
    if not request.is_json:
        return jsonify({"message": "Body is required"}), 400

    medicine = None

    try:
        medicine = add_medicine(request)
    except ValueError as err:
        return jsonify({"message": str(err)}), 400
    except ItemAlreadyExistsError as err:
        return jsonify({"messgae": str(err)}), 409

    return jsonify(medicine), 201

@app.route('/medicine', methods=['GET'])
def get_medicines():
    medicines = None

    try:
        medicines = get_all_medicines()
    except NotFoundError as err:
        return jsonify({"message": str(err)}), 404

    return jsonify(medicines), 200

@app.route('/medicine/<medicine_id>', methods=['GET'])
def get_by_id(medicine_id):
    regex = re.compile('[\w]{8}(-[\w]{4}){3}-[\w]{12}\Z')
    is_correct_id = regex.match(medicine_id)

    if not is_correct_id:
        return jsonify({'message': 'Invalid id provided' }), 400

    try:
        medicine = get_medicine_by_id(medicine_id)

        return jsonify(medicine), 200
    except NotFoundError as err:
        return jsonify({"message": str(err)}), 404

@app.route('/medicine/<medicine_id>', methods=['PUT'])
def update(medicine_id):
    regex = re.compile('[\w]{8}(-[\w]{4}){3}-[\w]{12}\Z')
    is_correct_id = regex.match(medicine_id)

    if not is_correct_id:
        return jsonify({'message': 'Invalid id provided' }), 400

    try:
        medicine = update_medicine(request, medicine_id)

        return jsonify(medicine), 200
    except NotFoundError as err:
        return jsonify({"message": str(err)}), 404

@app.route('/medicine/<medicine_id>', methods=['DELETE'])
def delete(medicine_id):
    regex = re.compile('[\w]{8}(-[\w]{4}){3}-[\w]{12}\Z')
    is_correct_id = regex.match(medicine_id)

    if not is_correct_id:
        return jsonify({'message': 'Invalid id provided' }), 400

    try:
        delete_medicine(medicine_id)

        return jsonify(), 200
    except NotFoundError as err:
        return jsonify({"message": str(err)}), 404