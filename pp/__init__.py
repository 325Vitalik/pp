__version__ = '0.1.0'
from flask import Flask
from wsgiref.simple_server import make_server

app = Flask(__name__)

@app.route('/')
def init():
    return 'It\'s ALIVE!!!'

@app.route('/api/v1/hello-world-31')
def hello_world():
    return 'Hello World 31'

server = make_server('', 3000, app)
print('Server is running on http://localhost:3000')
server.serve_forever()