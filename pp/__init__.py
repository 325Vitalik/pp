__version__ = '0.1.0'
from flask import Flask
app = Flask(__name__)

@app.route('/api/v1/hello-world-31')
def hello_world():
    return 'Hello World 31'