
""" Import Statements """

# Classics
import os
import pandas as pd
import pickle
import numpy as np

import re
import spacy
from spacy.tokenizer import Tokenizer
from collections import Counter

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('app/data/csv/cannabis.csv')

print('Shape:', df.shape)
print(df.head())

## spaCy
TOKENIZE_FILEPATH =  'app/data/pickled_models/tokenize.pkl'

#Loading the pickled models
tokenize = None

def pickleLoad():
    return pickle.load(open(TOKENIZE_FILEPATH,"rb" ))

tokenize = pickleLoad()

print("Open tokenize")

# Instantiate vectorizer object
tfidf = TfidfVectorizer(stop_words='english',
                        ngram_range=(1,3),
                        max_df=.97,
                        min_df=3,
                        tokenizer=tokenize,
                        max_features = 5000)

# Create a vocabulary and get word counts per document
dtm = tfidf.fit_transform(df['Type'] + df['Description'] + df['Effects'] + df['Flavors']) # Similiar to fit_predict

# Get feature names to use as dataframe column headers
dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())

# View Feature Matrix as DataFrame
print(dtm.head())

# Create cosine_similarity function
def cosine_recommender(user_input):

    user_dtm = pd.DataFrame(tfidf.transform([user_input]).todense(), columns=tfidf.get_feature_names())
    rec_dtm = dtm.append(user_dtm).reset_index(drop=True)
    cosine_df = pd.DataFrame(cosine_similarity(rec_dtm))
    recommendations = cosine_df[cosine_df[0] < 1][len(cosine_df)-1].sort_values(ascending=False)[:5]

    return recommendations

print(cosine_recommender(user_input))

# pickle new model
TFIDF_FILEPATH = os.path.join(os.path.dirname(__file__), "..","app", "data", "pickled_models", "tfidf.pkl")

with open(TFIDF_FILEPATH, "wb") as model_file:
  print("SAVE PICKLE 2")
  pickle.dump(tfidf, model_file, protocol=pickle.HIGHEST_PROTOCOL)

DTM_FILEPATH = os.path.join(os.path.dirname(__file__), "..","app", "data", "pickled_models", "dtm.pkl")

with open(DTM_FILEPATH, "wb") as model_file:
  print("SAVE PICKLE 3")
  pickle.dump(dtm, model_file, protocol=pickle.HIGHEST_PROTOCOL)

#Testing model
DTM_FILEPATH =  'app/data/pickled_models/dtm.pkl'
TFIDF_FILEPATH = 'app/data/pickled_models/tfidf.pkl'

#Loading the pickled models
tfidf_model = pickle.load(open(TFIDF_FILEPATH, 'rb'))
dtm_model = pickle.load(open(DTM_FILEPATH, 'rb'))

print(tfidf_model)
print(dtm_model)

def cosine_recs(user_input):
    user_dtm1 = pd.DataFrame(tfidf_model.transform([user_input]).todense(), columns=tfidf_model.get_feature_names())
    rec_dtm1 = dtm_model.append(user_dtm1).reset_index(drop=True)
    cosine_df1 = pd.DataFrame(cosine_similarity(rec_dtm1))
    recommendations5 = cosine_df1[cosine_df1[0] < 1][len(cosine_df)-1].sort_values(ascending=False)[1:6]
    rec_results = recommendations5.index.tolist()

    return rec_results

user_input = "creative headache"
#[992, 1330, 1419, 1097, 601]
print(cosine_recs(user_input))

