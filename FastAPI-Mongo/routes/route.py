from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId


route = APIRouter()

# Get Request 
@route.get("/")
async def get_todos():

    todos = list_serial(collection_name.find())
    return todos

@route.post("/")
async def post_todo(todo: Todo):

    collection_name.insert_one(dict(todo))
    return "Inserted"

@route.put("/{id}")
async def put_todo(id: str, todo: Todo):
    
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    # result = collection_name.find({"_id":ObjectId(id)})
    # return result
    return "Updated Successfully"
    
@route.delete("/{id}")
async def delete_todo(id: str):

    collection_name.find_one_and_delete({"_id":ObjectId(id)})
    # val = collection_name.find_one_and_delete({"_id":ObjectId(id)})
    # return val
