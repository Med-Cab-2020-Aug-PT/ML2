#app/model.py

"""
NLP Model for DS Build Week
Input  --> TF-IDF -->  Cosine_Similarity --> Output
Input  --> TF-IDF -->  Nearest Neighbor --> Output
"""

import pandas as pd
import os
from os import getenv

from pymongo import MongoClient

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv

load_dotenv()

DB_USER = getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = getenv("MONGO_PASSWORD", default="OOPS")
DB_URI = getenv("MONGO_URI", default="OOPS")
DB_URL = getenv("MONGO_URL", default="OOPS")

# client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_URI}/test?retryWrites=true&w=majority")
client = MongoClient(f"{getenv('MONGO_URL')}")

FILEPATH =  os.path.join(os.path.dirname(__file__),'data', 'csv', 'cannabis.csv')

class PredictionBot:
    """NLP Bot for Cannabis Suggestion App"""

    db =  client.medcabinet.strains
    df = pd.read_csv(FILEPATH)

    tfidf = TfidfVectorizer()
    nn = NearestNeighbors(n_neighbors=1, n_jobs=1)
    tokens = tfidf.fit_transform(
        df['Description']
    )
    nearest = nn.fit(
        pd.DataFrame(tokens.todense(), columns=tfidf.get_feature_names())
    )

    def predict(self, user_input):
        return next(self.db.find({'_id': int(self.nearest.kneighbors(
            self.tfidf.transform([user_input]).todense()
            )[1][0][0])}))

if __name__ == "__main__":
    bot = PredictionBot()
    print(bot.predict("Some text in here.. "))

