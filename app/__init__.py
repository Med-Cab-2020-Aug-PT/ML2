# app/__init__.py

import os
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv

from app.model import PredictionBot
from app.routes.strain_routes import API

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

def create_app():
    APP = Flask(__name__)
    APP.config["MONGO_URI"] = MONGO_URL

    APP.register_blueprint(API)

    return APP

if __name__ == '__main__':
    
    my_app = create_app()
    my_app.run(debug=True)

