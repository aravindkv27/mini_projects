import pprint
from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

load_dotenv()

con_str = os.getenv("CONNECTION_STRING")

# print(con_str)

client = MongoClient(con_str)

learn_db = client.learnmongo

# collections = learn_db.list_collection_names()

# print(collections)

# Insert one value into collection
def insert_val():

    collection = learn_db.test
    value = {
        "Original Name" : "Aravind K V",
        "Gaming Name" : "MannyFortune27"
    }

    inserted_id = collection.insert_one(value).inserted_id

    print(inserted_id)

# Check if the there is database name production if not it create one.
prod = client['production']
# print(production)
per_coll = prod['person_collection']


# Insert multiple values into collection
def create_documents():

    Original_names = ["Aravind","Anirudhu","Atif","Harish"]
    gaming_name = ["Jirariya","Itachi Uchicha","Might Guy","Naruto Uzumaki"]
    ages = [20,21,21,20]

    docs =[]

    for on, gn, age in zip(Original_names,gaming_name,ages):
        doc ={
            "Original Name": on,
            "Gaming Name": gn,
            "Age":age
        }
        docs.append(doc)
    
    per_coll.insert_many(docs)

# dbs = client.list_database_names()

# print(dbs)

printer = pprint.PrettyPrinter()

# Query the collection
def find_all_people():

    people = per_coll.find()

    for person in people:

        printer.pprint(person)

# Find one doc from the collection
def find_one_ele():

    name = per_coll.find_one({"Original Name":"Aravind"})
    printer.pprint(name)

# Count all the documents from the collection
def count_doc():

    count = per_coll.count_documents(filter={})
    print("No of Gamers: ",count)

# Find value using id
def get_person_by_id(person_id):

    _id = ObjectId(person_id)
    person = per_coll.find_one({"_id":_id})
    printer.pprint(person)

# Find between range
def find_by_range(min_age,max_age):

    """
    SELECT Age FROM per_coll WHERE age >= 18 AND age<=18;
    """

    query = {
            "$and":[
                {"Age":{"$gte":min_age}},
                {'Age':{"$lte":max_age}}
            ]
        }
    

    person= per_coll.find(query).sort("age")

    for pe in person:

        printer.pprint(pe)

def find_by_column():

    columns = {'_id':0, "Original Name":1,"Gaming Name":1}
    values = per_coll.find({},columns)

    for val in values:

        printer.pprint(val)

# Update 
def update_person_by_id(person_id):

    _id = ObjectId(person_id)
    all_update = {
        "$set":{"new_field":True},
        "$inc":{"Age":1},
        # "$rename":{""}
    }

    per_coll.update_one({"_id":_id},all_update)

    update_value = per_coll.find_one({"_id":_id})

    printer.pprint(update_value)

# To delete the doc
def remove_using_update(person_id):

    _id = ObjectId(person_id)

    per_coll.update_one({"_id":_id},{"$unset":{"new_field":""}})

def replacing_doc(person_id):

    _id = ObjectId(person_id)

    new_doc = {
        "Gaming Name":"Jiraiya"
    }
    per_coll.replace_one({"_id":_id},new_doc)

def delete_by_id(person_id):

    _id = ObjectId(person_id)

    per_coll.delete_one({"_id":_id})

new_date={
    "_id":"636507401760a6027025d245",
    "Played games":["Valorant","COD","Fall Guys","GTA-V"]
}

def add_address_emb(person_id,new_data):

    _id = ObjectId(person_id)

    per_coll.update_one({"_id":_id},{"$addToSet":{"addresses":new_data}})


if __name__ == "__main__":

    # get_person_by_id("636507401760a6027025d245")
    # find_by_range(18,21)
    # find_by_column()
    # update_person_by_id("636507401760a6027025d245")
    # replacing_doc("636507401760a6027025d245")
    delete_by_id("636507df64db7f19640e0ca4")