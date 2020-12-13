from repository.models import *
from config import *
from validation_schemas.user_schemas import create_user_schema
from flask_inputs.validators import JsonSchema
from flask_inputs import Inputs
from exceptions.errors import *
from helpers.encriptionHelper import *


class ValidateNewUser(Inputs):
    json = [JsonSchema(schema=create_user_schema)]

def get_serializable_user(user):
    result = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'birthday': user.birthday,
        'email': user.email,
        'phone_number': user.phone_number,
        'role': user.role
    }

    return result


def add_user(request, role='user'):
    inputs = ValidateNewUser(request)
    if not inputs.validate():
        raise ValueError('Not valid')

    if User.query.filter_by(email=request.json.get('email', None)).first() != None:
        raise ItemAlreadyExistsError('User with this email already exists')

    user = User(**request.json, role=role)
    user.password = encrypt_password(user.password)
    session = Session()
    session.add(user)
    session.commit()

    return get_serializable_user(user)

def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user == None:
        raise NotFoundError('User with id: ' + user_id + ' not found')
    
    return get_serializable_user(user)