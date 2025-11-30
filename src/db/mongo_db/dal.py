from src.db.mongo_db.connection import Connection
from pymongo.errors import PyMongoError
from bson import ObjectId


class Dal:
    def __init__(self, default_collection: str):
        self.default_collection: str = default_collection
        self.connection: Connection = Connection()

    def insert_one(self, document: dict, collection_name=None):
        collection_name: str = collection_name or self.default_collection
        try:
            self.connection.db[collection_name].insert_one(document)
        except PyMongoError as e:
            print(e)

    def insert_many(self, collection_name, documents):
        return self.connection.db[collection_name].insert_many(documents)

    def find(self, collection_name, query):
        return self.connection.db[collection_name].find(query)

    def find_all(self, collection_name=None):
        collection_name: str = collection_name or self.default_collection
        return list(self.connection.db[collection_name].find())

    def find_all_without_id(self, collection_name=None):
        collection_name: str = collection_name or self.default_collection
        print(collection_name)
        return list(self.connection.db[collection_name].find({},{'_id':0}))

    def find_by_id(self, collection_name, doc_id):
        if type(doc_id) is str:
            return self.connection.db[collection_name].find_one({"_id": doc_id})
        return self.connection.db[collection_name].find_one({"_id": ObjectId(doc_id)})

    def update_one(self, collection_name, query, document):
        return self.connection.db[collection_name].update_one(query, document)

    def delete_one(self, query, collection_name=None):
        collection_name: str = collection_name or self.default_collection
        return self.connection.db[collection_name].delete_one(query)

    def delete_all(self, collection_name):
        return self.connection.db[collection_name].delete_many({})

    def count_documents(self, collection_name, query):
        return self.connection.db[collection_name].count_documents(query)
