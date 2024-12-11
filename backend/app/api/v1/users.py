from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic.v1 import EmailStr

from app.crud.user import create_user, authenticate_user
from app.models.token import Token
from app.schemas.users import UserCreate, UserLogin, UserResponse

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate):
    db_user = await create_user(user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User already exists")
    return db_user


@router.post("/login", response_model=Token, name="users.login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    user = UserLogin(email=EmailStr(form_data.username), password=form_data.password)
    access_token = await authenticate_user(user.email, user.password)
    if access_token is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    return Token(access_token=access_token, token_type="bearer")
