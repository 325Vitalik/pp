from validation_schemas.demand_schemas import create_demand_schema
from flask_inputs.validators import JsonSchema
from flask_inputs import Inputs
from repository.models import *
from services.user_service import get_serializable_user
from services.medicine_service import get_serializable_medicine
from config import *
from exceptions.errors import *

class ValidateNewDemand(Inputs):
    json = [JsonSchema(schema=create_demand_schema)]

def get_serializable_demand(demand, user, medicine):
    result = {
        'id': demand.id,
        'amount': demand.amount,
        'user_id': user.id,
        'user': get_serializable_user(user),
        'mecine_id': medicine.id,
        'medicine': get_serializable_medicine(medicine)
    }

    return result

def add_demand(request):
    inputs = ValidateNewDemand(request)
    if not inputs.validate():
        raise ValueError('Not valid')

    demand = Demand(**request.json, user_id=auth.current_user().id)

    user = User.query.filter_by(id=demand.user_id).first()
    if user == None:
        raise NotFoundError('User with id: ' + user_id + ' not found')

    medicine = Medicine.query.filter_by(id=demand.medicine_id).first()
    if medicine == None:
        raise NotFoundError('Medicine with id: ' + medicine_id + ' not found')

    session = Session()
    session.add(demand)
    session.commit()

    return get_serializable_demand(demand, user, medicine)