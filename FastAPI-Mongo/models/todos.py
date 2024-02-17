from pydantic import BaseModel

class Todo(BaseModel):

    firstname: str
    lastname: str
    todo_item: str
    complete: bool
    