import json
import os
from dotenv import load_dotenv
from exceptions import NotConfigured, FileConError, FileLogError
from src.models.mongo_connection import MongoConnection
from src.models.token_auth import Token
from src.models.run_server import RunServer
import logging


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


if config_json["logging"]:
    file_path = config_json["logging"].get("file")
    if file_path:
        try:
            logging.basicConfig(filename=file_path, encoding='utf-8', level=logging.INFO)
        except Exception as e:
            raise FileLogError(e)
logger = logging.getLogger(__name__)
