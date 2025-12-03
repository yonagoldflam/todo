from src.db.mongo_db.dal import Dal
from datetime import datetime
from bson import ObjectId
from src.models.todo_doc import ToDoDocument
from src.schemas.todo_schema import ToDoCreate, ToDoResponse, ToDoId


class ToDoManager:
    def __init__(self):
        self.dal = Dal(default_collection='todo')

    def get_all_todos(self, username: str) -> list[ToDoResponse]:
        todos = list(self.dal.find({'username': username}))
        todo_models: list[ToDoResponse] = [
            ToDoResponse(id=str(todo['_id']), username=todo['username'], todo=todo['todo'], date=str(todo['date'])) for
            todo in todos]
        return todo_models

    def insert_todo(self, todo: ToDoCreate, username: str) -> ToDoId:
        todo_doc = ToDoDocument(username=username, todo=todo.todo, date=datetime.now())
        result = self.dal.insert_one(todo_doc.model_dump())
        return ToDoId(new_id=str(result.inserted_id))

    def delete_todo(self, id: str) -> None:
        self.dal.delete_one({'_id': ObjectId(id)})

    def doc_exists_by_id(self, id: str) -> bool:
        return self.dal.count({'_id': ObjectId(id)}, limit=1) > 0

    def doc_exists_by_id_and_username(self, id: str, username: str) -> bool:
        return self.dal.count({'_id': ObjectId(id), 'username': username}, limit=1) > 0
