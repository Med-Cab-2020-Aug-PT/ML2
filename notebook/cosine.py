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

# Import cannabis data
df = pd.read_csv('app/data/csv/cannabis.csv')

print('Shape:', df.shape)
print(df.head())

# spaCy

#Open pickled tokenizer for tfidf model
#Loading the pickled models

tokenize = pickle.load(open('tokenize.pkl', 'rb'))
print('Open Pickle')

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
print(cosine_recommender(user_input))

# pickle TFIDF
pickle.dump(tfidf, open('tfidf.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)

# pickle DTM
pickle.dump(dtm, open('dtm.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)


#Testing function with pickled models
user_input =["I am feeling sluggish. I am looking for an ammonia flavored strain that will have me feeling happy and energetic"]

#Testing model
#Loading the pickled models
dtm_model = pickle.load(open('dtm.pkl', 'rb'))
tfidf_model = pickle.load(open('tfidf.pkl', 'rb'))

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
    rec_result = recommendations5.index.tolist()

    return rec_result

print(cosine_recs(user_input))

#Results of user input: [992, 439, 184, 1117, 45]