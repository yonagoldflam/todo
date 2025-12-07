from config import mongo_connection
from src.db.mongo_db.mongo_repo import MongoRepo
from src.db.repo import Repo
from src.schemas.user_schema import UserCreate


class UserService:
    def __init__(self):
        if mongo_connection:
            self.repo: Repo = MongoRepo(collection_name='users')

    def insert_new_user(self, user: UserCreate) -> None:
        doc = user.model_dump()
        self.repo.insert_one(doc)

    def find_by_username(self, username: str):
        return self.repo.find_one({'username': username})
