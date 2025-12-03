from src.db.mongo_db.connection import Connection
from pymongo.errors import PyMongoError


class Dal:
    def __init__(self, default_collection: str):
        self.default_collection: str = default_collection
        self.connection: Connection = Connection()

    def insert_one(self, document: dict, collection_name=None):
        collection_name: str = collection_name or self.default_collection
        try:
            return self.connection.db[collection_name].insert_one(document)
        except PyMongoError as e:
            print(e)

    def find(self, query: dict[str, str], sub_fields: dict[str, int] = None, collection_name= None):
        collection_name: str = collection_name or self.default_collection
        if sub_fields:
            try:
                return self.connection.db[collection_name].find(query, sub_fields)
            except PyMongoError as e:
                print(e)
        try:
            return self.connection.db[collection_name].find(query)
        except PyMongoError as e:
            print(e)

    def find_one(self, query, collection_name= None):
        collection_name: str = collection_name or self.default_collection
        try:
            return self.connection.db[collection_name].find_one(query)
        except PyMongoError as e:
            print(e)

    def delete_one(self, query, collection_name=None):
        collection_name: str = collection_name or self.default_collection
        try:
            return self.connection.db[collection_name].delete_one(query)
        except PyMongoError as e:
            print(e)

    def count(self, query, limit: int = None, collection_name= None):
        collection_name: str = collection_name or self.default_collection
        if limit:
            try:
                return self.connection.db[collection_name].count_documents(query, limit=limit)
            except PyMongoError as e:
                print(e)
        try:
            return self.connection.db[collection_name].count_documents(query)
        except PyMongoError as e:
            print(e)

    def free_query(self, collection_name= None):
        collection_name: str = collection_name or self.default_collection
        try:
            return self.connection.db[collection_name]
        except PyMongoError as e:
            print(e)
