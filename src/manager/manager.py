from src.db.mongo_db.dal import Dal
from src.models.todo_model import ToDoModel
from datetime import datetime

class Manager:
    def __init__(self):
        self.dal = Dal(default_collection='todo')

    def get_all_todos(self):
        return self.dal.find_all_without_id()

    def insert_todo(self, task):
        todo = ToDoModel(id=task['id'], todo=task['todo'], date=datetime.now().strftime('%Y-%m-%d %H:%M'))
        doc = todo.model_dump()
        self.dal.insert_one(doc)

    def delete_todo(self, id: str):
        self.dal.delete_one({'id': id})


