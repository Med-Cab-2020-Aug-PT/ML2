#  data/stats_model/mongo.py

import os
import pandas as pd

from  pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def make_db():
    db =  MongoClient(
        f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}"
        f"@{os.getenv('MONGO_URI')}/test?retryWrites=true&w=majority"
    ).strain_table.strain

    df = pd.read_csv('cannabis.csv')
    data = df.to_dict(orient='records')

    for strain in data:
        strain['Effects'] = strain['Effects'].split(',')
        strain['Flavors'] = strain['Flavors'].split(',')
        strain['Nearest'] = [data[int(idx)]['Name'] for idx in strain['Nearest'].split(',')]

    db.insert_many(data)


if __name__ == "__main__":
    make_db()
