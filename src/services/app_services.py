from src.db.mongo_db.mongo_repo import MongoRepo
from src.services.todo_service import ToDoService
from src.services.user_service import UserService
from src.services.authenticate_service import Auth

class AppServices:
    todo = ToDoService(repo=MongoRepo(collection_name='todo'))
    user = UserService(repo=MongoRepo(collection_name='users'))
    auth = Auth()

services = AppServices()
