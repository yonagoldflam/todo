from pydantic import BaseModel

class RunServer(BaseModel):
    host: str
    port: int
