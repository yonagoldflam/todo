import json
import os
from dotenv import load_dotenv
from exceptions import NotConfigured, FileConError, FileLogError
from src.models.mongo_connection import MongoConnection
from src.models.token_auth import Token
from src.models.run_server import RunServer
from src.logging.file_logger import FileLogger
from src.logging.elastic_logger import EsLogger


load_dotenv()

config_path = os.getenv("CONFIG_PATH")

if not config_path:
    raise NotConfigured()

try:
    with open(config_path, "r") as f:
        config_json = json.load(f)
except:
    raise FileConError()

run_server = RunServer(**config_json["server"])
mongo_connection = config_json.get("mongo")
if mongo_connection:
    db_model = MongoConnection(**mongo_connection)
token_model = Token(**config_json["jwt"])


log_type = config_json.get("logging")
if log_type:
    if log_type.get("file"):
        logger = FileLogger(**log_type["file"]).get_logger()

    elif log_type.get("elastic"):
        logger = EsLogger(**config_json["logging"]["elastic"]).get_logger()
