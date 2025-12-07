from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
import uvicorn as uv
from fastapi.security import OAuth2PasswordRequestForm
from src.services.app_services import AppServices
from src.models.token_payload import TokenPayload
from src.schemas.todo_schema import ToDoResponse, ToDoCreate, ToDoId, DeleteTodo
from src.schemas.token_schema import TokenResponse
from src.schemas.user_schema import UserCreate, UserLogin
from config import run_server

app = FastAPI()

user_router = APIRouter(prefix="/users", tags=["Users"])
todo_router = APIRouter(prefix="/todos", tags=["Todos"])

services = AppServices()

@user_router.post("/", status_code=status.HTTP_201_CREATED)
def add_user(user: UserCreate):
    user.password = services.auth.hash_password(user.password)
    services.user.insert_new_user(user)


@user_router.post("/token", response_model=TokenResponse)
def login(user: OAuth2PasswordRequestForm = Depends()):
    user_doc = services.user.find_by_username(user.username)
    if not user_doc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='username does not exist in the system')

    if not services.auth.verify_password(password=user.password, hashed_password=user_doc['password']):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid password')

    token = services.auth.create_token(subject=user.username)
    return TokenResponse(access_token=token)

@user_router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    user_doc = services.user.find_by_username(user.username)
    if not user_doc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='username does not exist in the system')

    if not services.auth.verify_password(password=user.password, hashed_password=user_doc['password']):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid password')

    token = services.auth.create_token(subject=user.username)
    return TokenResponse(access_token=token)


@todo_router.get("/", response_model=list[ToDoResponse])
def get_all_tasks(token_payload: TokenPayload = Depends(services.auth.verify_token)):
    return services.todo.get_all_todos(token_payload.sub)


@todo_router.post("/", response_model=ToDoId)
def new_todo(todo: ToDoCreate, token_payload: TokenPayload = Depends(services.auth.verify_token)):
    new_id: ToDoId = services.todo.insert_todo(todo=todo, username=token_payload.sub)
    return new_id


@todo_router.delete("/{todo_id}")
def delete_todo(todo_id: str, token_payload: TokenPayload = Depends(services.auth.verify_token)):
    if not services.todo.doc_exists_by_id(todo_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'not found todo document with that id: {todo_id}')
    if not services.todo.doc_exists_by_id_and_username(todo_id, token_payload.sub):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'the username {token_payload.sub} does not have access to the todo document')
    services.todo.delete_todo(todo_id)
    return DeleteTodo()

app.include_router(user_router)
app.include_router(todo_router)


if __name__ == '__main__':
    uv.run('app:app', host=run_server.host, port=run_server.port, reload=True)
