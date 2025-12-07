from pydantic import BaseModel

class MongoConnection(BaseModel):
    host: str
    port: str
    user: str
    password: str
    db_name: str
    auth_db: str
