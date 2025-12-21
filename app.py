from fastapi import FastAPI, HTTPException, Request
import uvicorn as uv
from starlette.responses import JSONResponse
from config import run_server
from src.routs.user_routs import user_router
from src.routs.todo_routs import todo_router
from config import logger


app = FastAPI()

app.include_router(user_router)
app.include_router(todo_router)


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP status: {exc.status_code} detail: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


if __name__ == '__main__':
    uv.run('app:app', host=run_server.host, port=run_server.port, reload=True)
