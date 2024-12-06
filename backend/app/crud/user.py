from app.database.database import get_database
from app.schemas.user import UserCreate, UserLogin, UserResponse
import bcrypt
from pydantic import EmailStr

from datetime import datetime, timedelta

from app.core.config import settings
from app.utils.jwt_helper import create_access_token


async def create_user(user: UserCreate):
    db = get_database()
    user_collection = db['users']
    existing_user = await user_collection.find_one({"email": user.email})
    if existing_user:
        return None

    hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_dict = user.dict()
    user_dict['password'] = hashed_password.decode('utf-8')
    await user_collection.insert_one(user_dict)
    return UserCreate(**user_dict)


async def authenticate_user(email: EmailStr, password: str):
    db = get_database()
    user_collection = db['users']

    user_data = await user_collection.find_one({"email": email})
    if user_data and bcrypt.checkpw(password.encode(), user_data['password'].encode()):
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = await create_access_token(
            data={
                "sub": user_data['email'],
                "name": user_data['name'],
                "is_admin": user_data['is_admin']
            }, expires_delta=access_token_expires
        )
        return access_token

    return None
