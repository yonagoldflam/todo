from datetime import datetime

from pydantic import BaseModel

class ToDoDocument(BaseModel):
    username: str
    todo: str
    date: datetime