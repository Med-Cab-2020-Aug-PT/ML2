# tokenize with en_core_web_md
"""Import Statements"""
import os
import pickle
import re
import spacy

nlp = spacy.load("en_core_web_md")

STOP_WORDS = nlp.Defaults.stop_words.union({"$", '-', '', ' ',
                                            'bred','breed', 'breeds','call', 'calls',
                                            'combine', 'combines','consumer', 'contains','containing',
                                            "don't", 'effect', 'effects','especially','explanations',
                                            'flavor', 'flavors','flower','give', 'gives','got',  'high',
                                            'i', "i'm", "i've",'including','it.', "it's",
                                            'like', 'match', 'matches','making',
                                            'offer', 'offers','pack', 'packs','price', 'probably',
                                            'produce', 'produces', 'really',
                                            'refers', 'report', 'reports', "'s", 's',
                                            'seed', 'seeds','showing',
                                            'smell','start', 'started', 'stem', 'stems',
                                            'strain', 'strains','supposedly',
                                            'technique', 'techniques','tend', 'tends',
                                            'unavailable', 'unkown', 'user', 'users', 'utlizing',
                                            'weed', 'week', None})

def tokenize(text):
  doc = nlp(text) #casting as text
  return [token.lemma_.strip() for token in doc if not token.is_stop and not token.is_punct]


MODEL_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "app", "data", "pickled_models", "tokenize.pkl")

def pickleStore():
    pickle.dump(tokenize, open(MODEL_FILEPATH, "wb"), protocol=pickle.HIGHEST_PROTOCOL)

tokenize = pickleStore()