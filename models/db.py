from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import db_config

async_engine = create_async_engine(
    url=db_config.async_url,
    echo=db_config.sqla.echo,
    pool_size=db_config.sqla.pool_size,
    max_overflow=db_config.sqla.max_overflow,
)

async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)