from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from models.db import async_session
from models.user import User
from api.crud import post as post_crud
from api.schemas.post import PostCreate, PostResponse

router = APIRouter()

async def get_db():
    async with async_session() as session:
        yield session

@router.get("/posts", response_model=List[PostResponse])
async def get_posts(db: AsyncSession = Depends(get_db)):
    return await post_crud.get_posts(db)

@router.post("/posts", response_model=PostResponse)
async def create_post(
    post_data: PostCreate,
    db: AsyncSession = Depends(get_db)
):
    # Проверка что пользователь существует
    user = await db.get(User, post_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return await post_crud.create_post(db, post_data)