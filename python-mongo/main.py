from http import client
from pydoc import cli
from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

load_dotenv()

con_str = os.getenv("CONNECTION_STRING")

# print(con_str)

client = MongoClient(con_str)

learn_db = client.learnmongo

collections = learn_db.list_collection_names()

print(collections)

def insert_val():

    collection = learn_db.test
    value = {
        "Original Name" : "Aravind K V",
        "Gaming Name" : "MannyFortune27"
    }

    inserted_id = collection.insert_one(value).inserted_id

    print(inserted_id)

# Check if the there is database name production if not it create one.
production = client.production
person_collection = production.person_collection

dbs = client.list_database_names()

print(dbs)

if __name__ == "__main__":

    insert_val()