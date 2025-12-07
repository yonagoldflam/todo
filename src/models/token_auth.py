from pydantic import BaseModel


class Token(BaseModel):
    secret_key: str
    algo: str
    exp_token: float
