from validation_schemas.buy_schemas import create_buy_schema
from flask_inputs.validators import JsonSchema
from flask_inputs import Inputs
from repository.models import *
from services.user_service import get_serializable_user
from services.medicine_service import get_serializable_medicine
from config import *
from exceptions.errors import *

class ValidateNewBuy(Inputs):
    json = [JsonSchema(schema=create_buy_schema)]

def get_serializable_buy(buy, user, medicine):
    result = {
        'id': buy.id,
        'amount': buy.amount,
        'user_id': user.id,
        'user': get_serializable_user(user),
        'mecine_id': medicine.id,
        'medicine': get_serializable_medicine(medicine)
    }

    return result

def add_buy(request):
    inputs = ValidateNewBuy(request)
    if not inputs.validate():
        raise ValueError('Not valid')

    buy = Buy(**request.json, user_id=auth.current_user().id)

    user = User.query.filter_by(id=buy.user_id).first()
    if user == None:
        raise NotFoundError('User with id: ' + user_id + ' not found')

    medicine = Medicine.query.filter_by(id=buy.medicine_id).first()
    if medicine == None:
        raise NotFoundError('Medicine with id: ' + medicine_id + ' not found')

    if medicine.amount < buy.amount:
        raise NotFoundError('Medicines are not enough')

    session = Session()
    session.add(buy)
    session.commit()

    return get_serializable_buy(buy, user, medicine)