from services.buy_service import *
from config import *
from exceptions.errors import *

@app.route('/buy', methods=['POST'])
def create_buy():
    if not request.is_json:
        return jsonify({"message": "Body is required"}), 400

    try:
        buy = add_buy(request)

        return jsonify(buy), 201
    except ValueError as err:
        return jsonify({"message": str(err)}), 400
    except NotFoundError as err:
        return jsonify({"message": str(err)}), 404