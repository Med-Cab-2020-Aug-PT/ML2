#  data/mongo.py

import os
from  pymongo import MongoClient
import pandas as import pd
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority")

def setup_db():
    db =  client.strain
    df = pd.read_csv('cannabis.csv')
    data = df.to_dict(orient='records')

    for strain in data:
        strain['Effects'] = strain['Effects'].split(',')
        strain['Flavors'] = strain['Flavors'].split(',')
        strain['Nearest'] = [data[int(idx)]['Name'] for idx in strain['Nearest'].split(',')]

    db.insert_many(data)


if __name__ == "__main__":
    make_db()
    