from services.demand_service import *
from config import *
from exceptions.errors import *

@app.route('/demand', methods=['POST'])
@auth.login_required(role="user")
def create_demand():
    if not request.is_json:
        return jsonify({"message": "Body is required"}), 400

    try:
        demand = add_demand(request)

        return jsonify(demand), 201
    except ValueError as err:
        return jsonify({"message": str(err)}), 400
    except NotFoundError as err:
        return jsonify({"message": str(err)}), 404