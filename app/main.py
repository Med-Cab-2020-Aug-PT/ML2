#app/main.py

from flask import Flask, request, render_template, flash, redirect, jsonify
import os
from  app.controller import PredictionBot

__all__ = ('API',)
API = Flask(__name__)

@API.route('/')
def index():
    return jsonify("App Online")

@API.route('/search/<user_input>')
def search(user_input):
    """Utilizing NLP, users can type what they are looking for and the
    Predictionbot will find the closest match to their input"""
    bot = PredictionBot()
    return jsonify(bot.recommender(user_input))

@API.route('/name/<user_input>', methods=["POST"])
def name_lookup(user_input: str):
    """ Arbitrary Search Route """
    bot = PredictionBot()
    print(user_input)
    return jsonify(bot.name_lookup(user_input))

@API.route('/hello/')
@API.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# @API.route('/search/<user_input>')
# def search(user_input):
#     """Utilizing NLP, users can type what they are looking for and the
#     Predictionbot will find the closest match to their input"""
#     bot = PredictionBot()
#     return jsonify(bot.recommender(user_input))

if __name__ == "__main__":
    API.run(debug=True)