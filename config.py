from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = URL = os.getenv("URL")

db = SQLAlchemy(app)
engine = db.engine
Base = db.Model
#Session = sessionmaker(bind=engine)