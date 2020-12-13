from services.demand_service import *
from config import *

@app.route('/demand', methods=['POST'])
def create_demand():
    if not request.is_json:
        return jsonify({"message": "Body is required"}), 400

    try:
        demand = add_demand(request)

        return jsonify(demand), 201
    except ValueError as err:
        return jsonify({"message": str(err)}), 400