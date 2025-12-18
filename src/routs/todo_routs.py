from fastapi import Depends, APIRouter
from src.services.app_services import services
from src.models.token_payload import TokenPayload
from src.schemas.todo_schema import ToDoResponse, ToDoCreate, ToDoId, DeleteTodo

todo_router = APIRouter(prefix="/todos", tags=["Todos"])


@todo_router.get("/", response_model=list[ToDoResponse])
def get_all_tasks(token_payload: TokenPayload = Depends(services.auth.verify_token)):
    return services.todo.get_all_todos(token_payload.sub)


@todo_router.post("/", response_model=ToDoId)
def new_todo(todo: ToDoCreate, token_payload: TokenPayload = Depends(services.auth.verify_token)):
    new_id: ToDoId = services.todo.insert_todo(todo=todo, username=token_payload.sub)
    return new_id


@todo_router.delete("/{todo_id}")
def delete_todo(todo_id: str, token_payload: TokenPayload = Depends(services.auth.verify_token)):
    services.todo.doc_exists_by_id(todo_id)
    services.todo.doc_exists_by_id_and_username(todo_id, token_payload.sub)
    services.todo.delete_todo(todo_id)
    return DeleteTodo()
