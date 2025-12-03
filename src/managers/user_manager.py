
from src.db.mongo_db.dal import Dal
from src.authenticate.authenticate import Auth
from src.schemas.user_schema import UserCreate


class UseerManager:
    def __init__(self):
        self.dal = Dal(default_collection='users')
        self.auth = Auth()

    def insert_new_user(self, user: UserCreate) -> None:
        doc = user.model_dump()
        self.dal.insert_one(doc)

    def find_by_username(self, username: str):
        return self.dal.find_one({'username': username})
