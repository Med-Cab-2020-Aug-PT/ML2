#app/model.py

"""
NLP Model for DS Build Week
Input  --> TF-IDF -->  Cosine_Similarity --> Output
Input  --> TF-IDF -->  Cosine_Similarity --> Output
"""

import pandas as pd 
import os

from pymongo import MongoClient

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity 

from dotenv import load_dotenv

load_dotenv()

class PredictionBot:
    """NLP Bot for Cannabis Suggestion App"""

    def predict(self, user_input):
        return {
            '_id': 0, 
            'Name': 'Sour_Diesel', 
            'Effects': ['High', 'Happy', 'Hungry', 'Sleepy'],
            'Flavors': ['Sour', 'Fuel', 'Apple'],
            'Description': 'Sour Diesel is an aphrodisiac that produces a thick cloud', 
            'Nearest': ['Diesel', 'Sour Apple', 'Cherry Pie', 'Kush', 'Pineapple Express'], 
            'Rating': 4.7,
            'Type': 'Hybrid', 
        }

if __name__ == "__main__":
    bot = PredictionBot()
    print(bot.predict("Some text in here.. "))

