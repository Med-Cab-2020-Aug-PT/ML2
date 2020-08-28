""" Import Statements """

# Classics
import os
import pandas as pd
import pickle
import numpy as np

import re
import spacy
from spacy.tokenizer import Tokenizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('app/data/csv/cannabis.csv')

print('Shape:', df.shape)
print(df.head())

## spaCy
TOKENIZE_FILEPATH =  'app/data/pickled_models/tokenize.pkl'

#Loading the pickled models
tokenize = pickle.load(open(TOKENIZE_FILEPATH, 'rb'))
print(tokenize)

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
import json

def cosine_recommender(user_input):

    user_dtm = pd.DataFrame(tfidf.transform(user_input).todense(), columns=tfidf.get_feature_names())
    rec_dtm = dtm.append(user_dtm).reset_index(drop=True)
    cosine_df = pd.DataFrame(cosine_similarity(rec_dtm))
    recommendations = cosine_df[cosine_df[0] < 1][0].sort_values(ascending=False)[:5]

    return recommendations

user_input =["I am feeling sluggish. I am looking for an ammonia flavored strain that will have me feeling happy and energetic"]

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
    '''
    Function takes user input and transforms into vectorized dataframe
    This is then added to the dtm 
    Then it  calculates the similarity between input and strain 
    and returns the id of the top 5 closest matches.  
    '''
    #Vectorizes user input
    user_dtm1 = pd.DataFrame(tfidf_model.transform(user_input).todense(), columns=tfidf_model.get_feature_names())

    #Adds  transformed input to dtm
    rec_dtm1 = dtm_model.append(user_dtm1).reset_index(drop=True)

    #Calculates similarity and input
    cosine_df1 = pd.DataFrame(cosine_similarity(rec_dtm1))

    #Finds 5 closet strains.
    recommendations5 = cosine_df1[cosine_df1[0] < 1][0].sort_values(ascending=False)[:5]

    #Just grab index numbers
    rec_result = recommendations5.index.list()

    return rec_result

print(cosine_recs(user_input))

#Results of user input: [992, 439, 184, 1117, 45]