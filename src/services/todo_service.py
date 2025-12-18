from datetime import datetime
from src.db.repo import Repo
from src.models.todo_doc import ToDoDocument
from src.schemas.todo_schema import ToDoCreate, ToDoResponse, ToDoId
from exceptions import DocNotExist, NotAuthUser, DateFormatError


class ToDoService:
    def __init__(self, repo: Repo):
        self.repo = repo

    def get_all_todos(self, username: str) -> list[ToDoResponse]:
        todos = self.repo.find_all({'username': username})
        todo_models: list[ToDoResponse] = [ToDoResponse(**todo) for todo in todos]
        return todo_models

    def insert_todo(self, todo: ToDoCreate, username: str) -> ToDoId:
        due_date = self.format_datetime(todo.due_date)
        todo_doc = ToDoDocument(username=username, todo=todo.todo, due_date=due_date, date=datetime.now())
        new_id = self.repo.insert_one(todo_doc.model_dump())
        return ToDoId(new_id=new_id)

    def delete_todo(self, id: str) -> None:
        self.repo.delete_one({'_id': id})

    def doc_exists_by_id(self, id: str) -> None:
        if not self.repo.exists({'_id': id}):
            raise DocNotExist()

    def doc_exists_by_id_and_username(self, id: str, username: str) -> None:
        if not self.repo.exists({'_id': id, 'username': username}):
            raise NotAuthUser()

    def format_datetime(self, date_time: str)-> datetime:
        try:
            return datetime.strptime(date_time, "%d/%m/%Y %H:%M")
        except ValueError as e:
            raise DateFormatError(e)
