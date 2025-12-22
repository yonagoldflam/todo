from config import logger
from bson import ObjectId
from src.db.mongo_db.connection import Connection
from pymongo.errors import PyMongoError
from src.db.repo import Repo
from exceptions import MongoException


logger = logger.getLogger(__name__)
class MongoRepo(Repo):
    def __init__(self, collection_name: str):
        self.collection_name: str = collection_name
        self.connection: Connection = Connection()

    def insert_one(self, document: dict) -> str:
        doc_id = document.get('_id')
        if doc_id:
            document['_id'] = ObjectId(doc_id)
        try:
            result = self.connection.db[self.collection_name].insert_one(document)
            logger.info(f"Inserted {result.inserted_id}")
            return str(result.inserted_id)
        except PyMongoError as e:
            raise MongoException(str(e))

    def find_all(self, query: dict = None) -> list:
        query = query or {}
        doc_id = query.get('_id')
        if doc_id:
            query['_id'] = ObjectId(doc_id)
        try:
            docs = list(self.connection.db[self.collection_name].find(query))
            logger.info(f"Found {len(docs)} documents")
        except PyMongoError as e:
            raise MongoException(str(e))

        for doc in docs:
            doc['id'] = str(doc['_id'])
            del doc['_id']
            if doc.get('date'):
                doc['date'] = str(doc['date'])
            if doc.get('due_date'):
                doc['due_date'] = str(doc['due_date'])
        return docs

    def find_one(self, query: dict = None):
        query = query or {}
        doc_id = query.get('_id')
        if doc_id:
            query['_id'] = ObjectId(doc_id)
        try:
            doc = self.connection.db[self.collection_name].find_one(query)
            logger.info(f"Found {doc} document")
            if doc:
                doc['id'] = str(doc['_id'])
                del doc['_id']
                if doc.get('date'):
                    doc['date'] = str(doc['date'])
                if doc.get('due_date'):
                    doc['due_date'] = str(doc['due_date'])
                return doc
        except PyMongoError as e:
            raise MongoException(str(e))

    def delete_one(self, query):
        doc_id = query.get('_id')
        if doc_id:
            query['_id'] = ObjectId(doc_id)
        try:
            res = self.connection.db[self.collection_name].delete_one(query)
            logger.info(f"Deleted {res.deleted_count} documents")
            return res
        except PyMongoError as e:
            raise MongoException(str(e))

    def exists(self, query) -> bool:
        doc_id = query.get('_id')
        if doc_id:
            query['_id'] = ObjectId(doc_id)
        try:
            res = self.connection.db[self.collection_name].count_documents(query, limit=1) > 0
            logger.info(f"doc {doc_id} exists")
            return res
        except PyMongoError as e:
            raise MongoException(str(e))
