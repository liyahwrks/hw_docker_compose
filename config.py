from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings
from sqlalchemy import URL
import os

sqla_naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

class PostgresConfig:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", "5432"))
        self.user = os.getenv("DB_USER", "postgres")
        self.password = os.getenv("DB_PASSWORD", "password")


class SQLAlchemyConfig:
    def __init__(self):
        self.pool_size = int(os.getenv("SQLA_POOL_SIZE", "5"))
        self.max_overflow = int(os.getenv("SQLA_MAX_OVERFLOW", "10"))
        self.echo = os.getenv("SQLA_ECHO", "False").lower() == "true"


class DatabaseConfig:
    def __init__(self):
        self.pg = PostgresConfig()
        self.sqla = SQLAlchemyConfig()
    
    def build_url(self, driver: str) -> str:
        """Просто возвращаем строку URL"""
        return f"{driver}://{self.pg.user}:{self.pg.password}@{self.pg.host}:{self.pg.port}"
    
    @property
    def async_url(self) -> str:
        return self.build_url("postgresql+asyncpg")


db_config = DatabaseConfig()