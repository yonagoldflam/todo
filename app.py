from fastapi import FastAPI
import uvicorn as uv
from src.manager.manager import Manager

app = FastAPI()
manager = Manager()

@app.get("/todos")
def get_all_tasks():
    return manager.get_all_todos()

@app.post("/todo")
def new_todo(todo: dict[str, str]):
    manager.insert_todo(todo)

@app.delete("/delete")
def delete_todo(id: str):
    manager.delete_todo(id)

if __name__ == '__main__':
    uv.run('app:app', host='127.0.0.1', port=8000,reload=True)
