from pydantic import BaseModel

class ToDoCreate(BaseModel):
    todo: str
    due_date: str

class ToDoResponse(BaseModel):
    id: str
    username: str
    todo: str
    due_date: str
    date: str

class ToDoId(BaseModel):
    new_id: str

class DeleteTodo(BaseModel):
    status: str = 'delete success'
