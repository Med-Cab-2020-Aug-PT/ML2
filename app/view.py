#app/main.py

from flask import Flask, request, render_template, redirect, jsonify
import os
from  app.controller import PredictionBot

__all__ = ('API',)
API = Flask(__name__)

BOT = PredictionBot()

@API.route('/')
def index():
    return render_template('home.html')

@API.route('/search', methods=['POST'])
def compute():
    """Utilizing NLP, users can type what they are looking for and the
    Predictionbot will find the closest match to their input"""
    effect1 = request.form['item1']
    effect2 = request.form['item2']
    flavor = request.form['item3']
    t_input = request.form['item4']

    query = effect1 + " " + effect2 + " " + flavor + " " + t_input
    result = BOT.recommender(query)
    return render_template('result.html', result=result)

@API.route('/name', methods=["POST"])
def name_lookup():
    """ Arbitrary Search Route """
    query2 = request.form['query2']
    result = BOT.name_lookup(query2)
    return render_template('result.html', result=result)

if __name__ == "__main__":
    API.run(debug=True)