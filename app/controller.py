#app/controller.py
"""
NLP Model for DS Build Week
Input  --> TF-IDF -->  Cosine_Similarity --> Output
"""

import os
import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.model import StrainData
from dotenv import load_dotenv

__all__ = ('PredictionBot',)

load_dotenv()

FILEPATH =  os.path.join(os.path.dirname(__file__),'data', 'csv', 'cannabis.csv')
DTM_FILEPATH =  os.path.join(os.path.dirname(__file__),'data', 'pickled_models', 'dtm.pkl')
TFIDF_FILEPATH =  os.path.join(os.path.dirname(__file__),'data', 'pickled_models', 'tfidf.pkl')

class PredictionBot:
    """NLP Bot for Cannabis Suggestion App"""

    def __init__(self):
        self.data = StrainData()
        self.db =  self.data.connect_db()

        #Pickled models
        self.tfidf_model = pickle.load(open(TFIDF_FILEPATH, 'rb'))
        self.dtm_model = pickle.load(open(DTM_FILEPATH, 'rb'))

    def name_lookup(self, name: str) -> dict:
        return next(self.db.find({'Name': name.title()}))

    def recommender(self, user_input):
        user_dtm1 = pd.DataFrame(self.tfidf_model.transform([user_input]).todense(), columns=self.tfidf_model.get_feature_names())
        rec_dtm1 = self.dtm_model.append(user_dtm1).reset_index(drop=True)
        cosine_df1 = pd.DataFrame(cosine_similarity(rec_dtm1))

        recommendations5 = cosine_df1[cosine_df1[0] < 1][len(cosine_df1)-1].sort_values(ascending=False)[1:6]
        rec_result = recommendations5.index.tolist()

        mongo_recs = next(self.db.find({'_id':(rec_result)[0]}))
        return mongo_recs

if __name__ == "__main__":
    bot = PredictionBot()
    print(bot.recommender("big buds"))
    print(bot.name_lookup('Ocd'))

