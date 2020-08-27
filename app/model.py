#app/model.py

"""
NLP Model for DS Build Week
Input  --> TF-IDF -->  Cosine_Similarity --> Output
Input  --> TF-IDF -->  Nearest Neighbor --> Output
"""

import os
from os import getenv
import pandas as pd
import pickle

from pymongo import MongoClient

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv

load_dotenv()

FILEPATH =  os.path.join(os.path.dirname(__file__),'data', 'csv', 'cannabis.csv')
DTM_FILEPATH =  os.path.join(os.path.dirname(__file__),'data', 'pickled_models', 'dtm.pkl')
TFIDF_FILEPATH =  os.path.join(os.path.dirname(__file__),'data', 'pickled_models', 'tfidf.pkl')
TOKENIZE_FILEPATH =  os.path.join(os.path.dirname(__file__),'data', 'pickled_models', 'tokens.pkl')

class PredictionBot:
    """NLP Bot for Cannabis Suggestion App"""


    db =  MongoClient(f"{getenv('MONGO_URL')}").medcabinet.strains
    df = pd.read_csv(FILEPATH)

    #Pickled models
    tfidf_model = pickle.load(open(DTM_FILEPATH, 'rb'))
    dtm_model = pickle.load(open(TFIDF_FILEPATH, 'rb'))
    tokenize = pickle.load(open(TOKENIZE_FILEPATH, 'rb'))

    # def predict(self, user_input):
    #     return next(self.db.find({'_id': int(self.nearest.kneighbors(
    #         self.tfidf.transform([user_input]).todense()
    #         )[1][0][0])}))

    def cosine_recommender(self, user_input):
        user_dtm = pd.DataFrame(self.tfidf_model.transform(user_input).todense(), columns=tfidf_model.get_feature_names())
        rec_dtm = self.dtm_model.append(user_dtm1).reset_index(drop=True)
        cosine_df = pd.DataFrame(cosine_similarity(rec_dtm1))

        recommendations5 = next(self.db.find({'_id': int(cosine_df1[cosine_df1[0] < 1][0].sort_values(ascending=False)[:5])[1][0][0]}))
        return recommendations5

if __name__ == "__main__":
    bot = PredictionBot()
    print(bot.cosine_recommender("Some text in here.. "))

