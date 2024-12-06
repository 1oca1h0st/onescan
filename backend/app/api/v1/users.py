from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.crud.user import create_user, authenticate_user

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate):
    db_user = await create_user(user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User already exists")
    return db_user


@router.post("/login", response_model=UserResponse, name="users.login")
async def login_user(user: UserLogin):
    db_user = await authenticate_user(user)
    if db_user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    return db_user
