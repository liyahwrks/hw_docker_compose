from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from models.db import async_session
from api.crud import user as user_crud
from api.schemas.user import UserCreate, UserResponse

router = APIRouter()

async def get_db():
    async with async_session() as session:
        yield session

@router.get("/users", response_model=List[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    return await user_crud.get_users(db)

@router.post("/users", response_model=UserResponse)
async def create_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    return await user_crud.create_user(db, user_data)