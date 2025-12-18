from src.db.repo import Repo
from src.schemas.user_schema import UserCreate
from exceptions import UserNotFound, UserAlreadyExists


class UserService:
    def __init__(self, repo: Repo):
        self.repo = repo

    def insert_new_user(self, user: UserCreate):
        doc = user.model_dump()
        if self.repo.exists({'username' : user.username}):
            raise UserAlreadyExists()
        self.repo.insert_one(doc)

    def find_by_username(self, username: str):
        user_doc = self.repo.find_one({'username': username})
        if not user_doc:
            raise UserNotFound()
        return user_doc
