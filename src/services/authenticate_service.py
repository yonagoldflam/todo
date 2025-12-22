from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from src.models.token_payload import TokenPayload
from config import token_model
from exceptions import InvalidToken, InvalidPassword
from config import logger


logger = logger.getLogger(__name__)
class Auth:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")
    def __init__(self):
        self.secret_key = token_model.secret_key
        self.algorithm = token_model.algo
        self.exp_token = token_model.exp_token
        self.password_context = CryptContext(schemes=["argon2"], deprecated="auto")

    def create_token(self, subject):
        now = datetime.utcnow()
        expire = now + timedelta(minutes=self.exp_token)
        token_payload = TokenPayload(sub=subject, iat=now, exp=expire)
        token = jwt.encode(token_payload.model_dump(), self.secret_key, algorithm=self.algorithm)
        logger.info(f"token created: {token}")
        return token


    def hash_password(self, password: str) -> str:
        return self.password_context.hash(password)

    def verify_password(self, password: str, hashed_password: str) -> None:
        if not self.password_context.verify(password, hashed_password):
            raise InvalidPassword()

    def verify_token(self, token: str = Depends(oauth2_scheme)) -> TokenPayload:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            logger.info(f"token decoded success: {payload}")
            return TokenPayload(**payload)
        except jwt.PyJWTError as e:
            raise InvalidToken(e)
