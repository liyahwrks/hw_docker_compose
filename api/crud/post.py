from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.post import Post
from api.schemas.post import PostCreate

async def get_posts(db: AsyncSession):
    result = await db.execute(
        select(Post).order_by(Post.id.desc())
    )
    return result.scalars().all()

async def create_post(db: AsyncSession, post_data: PostCreate):
    post = Post(**post_data.model_dump())
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post