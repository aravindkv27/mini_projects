def individual_serial(todo) -> dict:

    return {
        "id": str(todo["_id"]),
        "firstname": todo["firstname"],
        "lastname": todo["lastname"],
        "todo_list": todo["todo_item"],
        "complete": todo["complete"]
    }


def list_serial(todos) -> list:

    return [individual_serial(todo) for todo in todos]