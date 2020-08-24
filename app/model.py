#app/model.py

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
        return "Output"

if __name__ == "__main__":
    bot = PredictionBot()
    print(bot.predict("Some text in here.. "))

