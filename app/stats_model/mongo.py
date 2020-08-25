#  data/stats_model/mongo.py

import os
import pandas as pd

from  pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_URI", default="OOPS")

client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}/test?retryWrites=true&w=majority")

def make_db():
    db =  client.strain_table.strain

    df = pd.read_csv('cannabis.csv')
    data = df.to_dict(orient='records')

    for strain in data:
        strain['Effects'] = strain['Effects'].split(',')
        strain['Flavors'] = strain['Flavors'].split(',')
        strain['Nearest'] = [data[int(idx)]['Name'] for idx in strain['Nearest'].split(',')]

    db.insert_many(data)


if __name__ == "__main__":
    make_db()
