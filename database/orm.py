from sqlalchemy import select, text, insert, func, cast
import asyncio
from database.database import sync_engine, async_engine, session_factory, async_session_factory
from database.db_model import Base

class AsyncORM():
    def __init__(self):
        pass

    @staticmethod
    async def create_tables():
        async_engine.echo = True
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        async_engine.echo = False

    @staticmethod
    async def insert_shopitem():
        async with async_session_factory() as session:
            pass

    @staticmethod
    async def select_shopitem():
        async_engine.echo = False
        async with async_session_factory() as session:
            pass

    @staticmethod
    async def update_shopitem():
        async_engine.echo = False
        async with async_session_factory() as session:
            pass
