from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import noload
from models.user import User
from api.schemas.user import UserCreate

async def get_users(db: AsyncSession):
    result = await db.execute(
        select(User).options(noload(User.posts))
    )
    return result.scalars().all()

async def create_user(db: AsyncSession, user_data: UserCreate):
    user = User(**user_data.model_dump())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user