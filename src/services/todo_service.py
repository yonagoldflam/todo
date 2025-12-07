from config import mongo_connection
from src.db.mongo_db.mongo_repo import MongoRepo
from datetime import datetime
from bson import ObjectId
from src.db.repo import Repo
from src.models.todo_doc import ToDoDocument
from src.schemas.todo_schema import ToDoCreate, ToDoResponse, ToDoId


class ToDoService:
    def __init__(self):
        if mongo_connection:
            self.repo: Repo = MongoRepo(collection_name='todo')

    def get_all_todos(self, username: str) -> list[ToDoResponse]:
        todos = list(self.repo.find_all({'username': username}))
        todo_models: list[ToDoResponse] = [
            ToDoResponse(id=str(todo['_id']), username=todo['username'], todo=todo['todo'], date=str(todo['date'])) for
            todo in todos]
        return todo_models

    def insert_todo(self, todo: ToDoCreate, username: str) -> ToDoId:
        todo_doc = ToDoDocument(username=username, todo=todo.todo, date=datetime.now())
        result = self.repo.insert_one(todo_doc.model_dump())
        return ToDoId(new_id=str(result.inserted_id))

    def delete_todo(self, id: str) -> None:
        self.repo.delete_one({'_id': ObjectId(id)})

    def doc_exists_by_id(self, id: str) -> bool:
        return self.repo.exists({'_id': ObjectId(id)})

    def doc_exists_by_id_and_username(self, id: str, username: str) -> bool:
        return self.repo.exists({'_id': ObjectId(id), 'username': username})
