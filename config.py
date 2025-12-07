import json
import os
from dotenv import load_dotenv
from src.models.mongo_connection import MongoConnection
from src.models.token_auth import Token
from src.models.run_server import RunServer

load_dotenv()

config_path = os.getenv("CONFIG_PATH")

if not config_path:
    raise ValueError("Config path not set")

with open(config_path, "r") as f:
    config_json = json.load(f)

run_server = RunServer(**config_json["server"])
mongo_connection = config_json.get("mongo")
if mongo_connection:
    db_model = MongoConnection(**mongo_connection)
token_model = Token(**config_json["jwt"])
