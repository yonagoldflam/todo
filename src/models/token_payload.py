from datetime import datetime
from typing import Union

from pydantic import BaseModel

class TokenPayload(BaseModel):
    sub: str
    iat: Union[int, datetime]
    exp: Union[int, datetime]
