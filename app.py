from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn as uv
from fastapi.security import OAuth2PasswordRequestForm

from src.authenticate.authenticate import Auth
from src.managers.user_manager import UseerManager
from src.managers.todo_manager import ToDoManager
from src.models.token_payload import TokenPayload
from src.schemas.todo_schema import ToDoResponse, ToDoCreate, ToDoId, DeleteTodo
from src.schemas.token_schema import TokenResponse
from src.schemas.user_schema import UserCreate, UserLogin

app = FastAPI()

auth = Auth()
user_manager = UseerManager()
todo_manager = ToDoManager()

@app.post("/new_user")
def add_user(user: UserCreate):
    user.password = auth.hash_password(user.password)
    user_manager.insert_new_user(user)


@app.post("/token", response_model=TokenResponse)
def login(user: OAuth2PasswordRequestForm = Depends()):
    user_doc = user_manager.find_by_username(user.username)
    if not user_doc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='username does not exist in the system')

    if not auth.verify_password(password=user.password, hashed_password=user_doc['password']):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid password')

    token = auth.create_token(subject=user.username)
    return TokenResponse(access_token=token)

@app.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    user_doc = user_manager.find_by_username(user.username)
    if not user_doc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='username does not exist in the system')

    if not auth.verify_password(password=user.password, hashed_password=user_doc['password']):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid password')

    token = auth.create_token(subject=user.username)
    return TokenResponse(access_token=token)


@app.get("/todos", response_model=list[ToDoResponse])
def get_all_tasks(token_payload: TokenPayload = Depends(auth.verify_token)):
    return todo_manager.get_all_todos(token_payload.sub)


@app.post("/todo", response_model=ToDoId)
def new_todo(todo: ToDoCreate, token_payload: TokenPayload = Depends(auth.verify_token)):
    new_id: ToDoId = todo_manager.insert_todo(todo=todo, username=token_payload.sub)
    return new_id


@app.delete("/delete")
def delete_todo(id: str, token_payload: TokenPayload = Depends(auth.verify_token)):
    if not todo_manager.doc_exists_by_id(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'not found todo document with that id: {id}')
    if not todo_manager.doc_exists_by_id_and_username(id, token_payload.sub):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'the username {token_payload.sub} does not have access to the todo document')
    todo_manager.delete_todo(id)
    return DeleteTodo()


if __name__ == '__main__':
    uv.run('app:app', host='127.0.0.1', port=8000, reload=True)
