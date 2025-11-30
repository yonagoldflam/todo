import datetime

from pydantic import BaseModel


class ToDoModel(BaseModel):
    id: str
    todo: str
    date: str