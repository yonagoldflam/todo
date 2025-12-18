import pymongo
from pymongo.errors import PyMongoError
from config import db_model
from exceptions import MongoException
import logging

class Connection:
    def __init__(self):
        try:
            mongo_user = db_model.user
            mongo_password = db_model.password
            mongo_db = db_model.db_name
            mongo_host = db_model.host
            mongo_port = db_model.port
            auth_db = db_model.auth_db

            self.client = pymongo.MongoClient(
                host=mongo_host,
                port=int(mongo_port),
                username=mongo_user,
                password=mongo_password,
                authSource=auth_db,
            )

            self.db = self.client[mongo_db]
            logging.info("Connection established")

        except PyMongoError as e:
            raise MongoException(str(e))
