from fastapi import FastAPI
from routes.route import route
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app  = FastAPI()

app.include_router(route)