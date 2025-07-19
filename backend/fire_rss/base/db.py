from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from ..config import config

engine = create_async_engine(**config.DB_ENGINE_CONFIG)
AsyncSessionFactory = async_sessionmaker(bind=engine, **config.DB_SESSION_MAKER_CONFIG)


@asynccontextmanager
async def get_session():
    async with AsyncSessionFactory() as session:
        yield session
