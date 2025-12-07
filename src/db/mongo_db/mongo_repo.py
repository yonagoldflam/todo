from src.db.mongo_db.connection import Connection
from pymongo.errors import PyMongoError
from src.db.repo import Repo


class MongoRepo(Repo):
    def __init__(self, collection_name: str):
        self.collection_name: str = collection_name
        self.connection: Connection = Connection()

    def insert_one(self, document: dict):
        try:
            return self.connection.db[self.collection_name].insert_one(document)
        except PyMongoError as e:
            print(e)

    def find_all(self, query: dict[str, str]):

        try:
            return self.connection.db[self.collection_name].find(query)
        except PyMongoError as e:
            print(e)

    def find_one(self, query):
        try:
            return self.connection.db[self.collection_name].find_one(query)
        except PyMongoError as e:
            print(e)

    def delete_one(self, query):
        try:
            return self.connection.db[self.collection_name].delete_one(query)
        except PyMongoError as e:
            print(e)

    def exists(self, query) -> bool:
        try:
            return self.connection.db[self.collection_name].count_documents(query, limit=1) > 0
        except PyMongoError as e:
            print(e)
        return False

