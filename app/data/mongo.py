#  data/stats_model/mongo.py

from os import getenv
import pandas as pd

from  pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

DB_USER = getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = getenv("MONGO_PASSWORD", default="OOPS")
DB_URI = getenv("MONGO_URI", default="OOPS")
DB_NAME = getenv("MONGO_DB", default ="OOPS")

client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_URI}/test?retryWrites=true&w=majority")

def make_db():

    db = client.medcabinet.strains
    df = pd.read_csv('../data/csv/cannabis.csv')
    data = df.to_dict(orient='records')

    for strain in data:
        strain['Effects'] = strain['Effects'].split(',')
        strain['Flavors'] = strain['Flavors'].split(',')
        strain['Nearest'] = [data[int(idx)]['Name'] for idx in strain['Nearest'].split(',')]

    db.insert_many(data)


if __name__ == "__main__":
    make_db()
