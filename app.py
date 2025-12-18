from fastapi import FastAPI
import uvicorn as uv
from config import run_server
from src.routs.user_routs import user_router
from src.routs.todo_routs import todo_router


app = FastAPI()

app.include_router(user_router)
app.include_router(todo_router)


if __name__ == '__main__':
    uv.run('app:app', host=run_server.host, port=run_server.port, reload=True)
