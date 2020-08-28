#app/main.py

from flask import Flask, request, render_template, flash, redirect, jsonify
import os
from  app.controller import PredictionBot

__all__ = ('API',)
API = Flask(__name__)
API.control = PredictionBot()

@API.route('/')
def index():
    return jsonify("App Online")

@API.route('/search/<user_input>')
def search(user_input):
    """Utilizing NLP, users can type what they are looking for and the
    Predictionbot will find the closest match to their input"""

    return jsonify(API.control.recommender(user_input))

@API.route('/name/<strain>')
def name_lookup(strain):
    """ Arbitrary Search Route """
    return jsonify(API.control.name_lookup(user_input))

if __name__ == "__main__":
    API.run(debug=True)