from fastapi import Depends, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from src.services.app_services import services
from src.schemas.token_schema import TokenResponse
from src.schemas.user_schema import UserCreate, UserLogin

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.post("/", status_code=status.HTTP_201_CREATED)
def add_user(user: UserCreate):
    user.password = services.auth.hash_password(user.password)
    services.user.insert_new_user(user)


@user_router.post("/token", response_model=TokenResponse)
def login(user: OAuth2PasswordRequestForm = Depends()):
    user_doc = services.user.find_by_username(user.username)
    services.auth.verify_password(password=user.password, hashed_password=user_doc['password'])
    token = services.auth.create_token(subject=user.username)
    return TokenResponse(access_token=token)


@user_router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    user_doc = services.user.find_by_username(user.username)
    services.auth.verify_password(password=user.password, hashed_password=user_doc['password'])
    token = services.auth.create_token(subject=user.username)
    return TokenResponse(access_token=token)
