from src.services.todo_service import ToDoService
from src.services.user_service import UserService
from src.services.authenticate_service import Auth

class AppServices:
    todo = ToDoService()
    user = UserService()
    auth = Auth()
