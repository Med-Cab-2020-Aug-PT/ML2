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