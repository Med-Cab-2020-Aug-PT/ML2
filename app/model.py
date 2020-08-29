#app/model.py

import pandas as pd
from  pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

__all__ = ('StrainData',)

load_dotenv()
DB_USER = getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = getenv("MONGO_PASSWORD", default="OOPS")
DB_URI = getenv("MONGO_URI", default="OOPS")


class StrainData():

    def connect_db(self):
        """MongoDB Table Connection"""
        return MongoClient(f"{getenv('MONGO_URL')}").medcabinet.strains

    def read_csv(self):
        pd.read_csv('../data/csv/cannabis.csv')

    def make_db(self):
        """Creates and Populates the Database"""
        db = self.connect_db()
        data = self.read_csv().to_dict(orient='records')

        for strain in data:
            strain['Effects'] = strain['Effects'].split(',')
            strain['Flavors'] = strain['Flavors'].split(',')
            strain['Nearest'] = [data[int(idx)]['Name'] for idx in strain['Nearest'].split(',')]

        db.insert_many(data)


if __name__ == "__main__":
    data_model = DataModel()
    # data_model._make_db()  # DO ONLY ONCE!
    print(next(data_model.connect_db().find({'Name': 'Caramelicious'})))
