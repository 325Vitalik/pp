from repository.models import *
from config import *
from validation_schemas.medicine_schemas import create_medicine_schema
from flask_inputs.validators import JsonSchema
from flask_inputs import Inputs
from exceptions.errors import *
from helpers.encriptionHelper import *

class ValidateNewMedicine(Inputs):
    json = [JsonSchema(schema=create_medicine_schema)]

def get_serializable_medicine(medicine):
    result = {
        'id': medicine.id,
        'name': medicine.name,
        'amount': medicine.amount,
        'price': medicine.price,
    }

    return result

def add_medicine(request):
    inputs = ValidateNewMedicine(request)
    if not inputs.validate():
        raise ValueError('Not valid')

    medicine = Medicine(**request.json)
    session = Session()
    session.add(medicine)
    session.commit()

    return get_serializable_medicine(medicine)

def get_all_medicines():
    medicines = Medicine.query.all()

    if len(medicines) == 0:
        raise NotFoundError('Medicines not found')

    return [get_serializable_medicine(i) for i in medicines]

def get_medicine_by_id(medicine_id):
    medicine = Medicine.query.filter_by(id=medicine_id).first()
    if medicine == None:
        raise NotFoundError('Medicine with id: ' + medicine_id + ' not found')
    
    return get_serializable_medicine(medicine)

def update_medicine(request, medicine_id):
    medicine = Medicine.query.filter_by(id=medicine_id).first()
    if medicine == None:
        raise NotFoundError('Medicine with id: ' + medicine_id + ' not found')

    inputs = ValidateNewMedicine(request)
    if not inputs.validate():
        raise ValueError('Not valid')

    newMedicine = Medicine(**request.json)

    medicine.name = newMedicine.name
    medicine.amount = newMedicine.amount
    medicine.price = newMedicine.price
    db.session.commit()

    return get_serializable_medicine(medicine)

def delete_medicine(medicine_id):
    medicine = Medicine.query.filter_by(id=medicine_id).first()
    if medicine == None:
        raise NotFoundError('Medicine with id: ' + medicine_id + ' not found')
    
    db.session.delete(medicine)
    db.session.commit()
