__version__ = '0.1.0'
from config import *

db.create_all()

from controllers.user_controller import *
from controllers.medicine_controller import *
from controllers.buy_controller import *
from controllers.demand_controller import *

@app.route('/')
def init():
    return 'It\'s ALIVE!!!'

if __name__ == '__main__':
    app.run()