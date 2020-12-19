__version__ = '0.1.0'
from config import *
from helpers.encriptionHelper import *
db.create_all()

from controllers.user_controller import *
from controllers.medicine_controller import *
from controllers.buy_controller import *
from controllers.demand_controller import *

@app.route('/')
def init():
    return 'It\'s ALIVE!!!'

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(email=username).first()
    if user and check_encrypted_password(password, user.password):
        return user

@auth.get_user_roles
def get_user_roles(user):
    return user.role

if __name__ == '__main__':
    app.run()