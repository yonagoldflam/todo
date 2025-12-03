from pydantic import BaseModel

class ToDoCreate(BaseModel):
    todo: str

class ToDoResponse(BaseModel):
    id: str
    username: str
    todo: str
    date: str

class ToDoId(BaseModel):
    new_id: str

class DeleteTodo(BaseModel):
    status: str = 'delete success'