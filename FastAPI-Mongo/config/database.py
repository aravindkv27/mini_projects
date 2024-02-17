from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

uri = os.getenv('CLIENT_URI')

client = MongoClient(uri)

db = client.todo_db

collection_name = db["todo_list"]