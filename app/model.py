#app/model.py

"""
NLP Model for DS Build Week
Input  --> TF-IDF -->  Cosine_Similarity --> Output
"""

import os
from os import getenv
import pandas as pd
import pickle

from pymongo import MongoClient

import spacy
from spacy.tokenizer import Tokenizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv

load_dotenv()

FILEPATH =  os.path.join(os.path.dirname(__file__),'data', 'csv', 'cannabis.csv')
DTM_FILEPATH =  os.path.join(os.path.dirname(__file__),'data', 'pickled_models', 'dtm.pkl')
TFIDF_FILEPATH =  os.path.join(os.path.dirname(__file__),'data', 'pickled_models', 'tfidf.pkl')

class PredictionBot:
    """NLP Bot for Cannabis Suggestion App"""

    def __init__(self):
        self.db =  MongoClient(f"{getenv('MONGO_URL')}").medcabinet.strains

        #Pickled models
        self.tfidf_model = pickle.load(open(TFIDF_FILEPATH, 'rb'))
        self.dtm_model = pickle.load(open(DTM_FILEPATH, 'rb'))

    def cosine_recommender(self, user_input):
        user_dtm1 = pd.DataFrame(tfidf_model.transform([user_input]).todense(), columns=tfidf_model.get_feature_names())
        rec_dtm1 = dtm_model.append(user_dtm1).reset_index(drop=True)
        cosine_df1 = pd.DataFrame(cosine_similarity(rec_dtm1))

        recommendations5 = cosine_df1[cosine_df1[0] < 1][0].sort_values(ascending=False)[:5]
        rec_result = recommendations.index.tolist()

        mongo_recs = next(self.db.find({'_id':(rec_result)[1]}))
        return mongo_recs

if __name__ == "__main__":
    bot = PredictionBot()
    print(bot.cosine_recommender("Some text in here.. "))

