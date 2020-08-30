#app/main.py

from flask import Flask, request, render_template, redirect, jsonify
import os
from  app.controller import PredictionBot

__all__ = ('API',)
API = Flask(__name__)

#need to make bot a global variable for other routes to use.

@API.route('/')
def index():
    return render_template('home.html')

@API.route('/search', methods=['POST'])
def search():
    """Utilizing NLP, users can type what they are looking for and the
    Predictionbot will find the closest match to their input"""
    query = request.form['query']
    bot = PredictionBot()
    return jsonify(bot.recommender(query))

@API.route('/name', methods=["POST"])
def name_lookup():
    """ Arbitrary Search Route """
    query = request.form['query']
    bot = PredictionBot()
    print(query)
    return jsonify(bot.name_lookup(query))

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