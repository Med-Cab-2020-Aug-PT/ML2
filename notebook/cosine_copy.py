""" Import Statements """

# Classics
import os
import pandas as pd
import pickle
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import squarify

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
# TOKENIZE_FILEPATH =  '../app/data/pickled_models/tokenize.pkl'
TOKENIZE_FILEPATH =  'notebook/tokenize.pkl'

#Loading the pickled models
tokenize = pickle.load(open(TOKENIZE_FILEPATH, 'rb'))

# Instantiate vectorizer object
tfidf = TfidfVectorizer(stop_words='english', 
                        ngram_range=(1,3),
                        max_df=.97,
                        min_df=3,
                        tokenizer=tokenize,
                        max_features = 5000)

# Create a vocabulary and get word counts per document
dtm = tfidf.fit_transform(df['Type'] + df['Description'] + df['Effects'] + df['Flavors']) # Similiar to fit_predict

# Print word counts

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

user_input1 =["I am feeling sluggish. I am looking for an ammonia flavored strain that will have me feeling happy and energetic"]
print(cosine_recommender(user_input1))