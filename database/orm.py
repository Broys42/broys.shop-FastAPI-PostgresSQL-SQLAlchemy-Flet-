from sqlalchemy import select, text, insert, func, cast
from sqlalchemy.orm import aliased
import asyncio
from database.database import sync_engine, async_engine, session_factory, async_session_factory
from database.db_model import Base
from database.db_model import User, ShopItem, Cart, CartItem


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
    async def insert_headphones(name, price, description, stock_quantity):
        async with async_session_factory() as session:
            headphones = ShopItem(name=name, price=price, description=description, stock_quantity=stock_quantity)
            session.add(headphones)
            await session.commit()

    @staticmethod
    async def delete_headphones(headphones_id):
        async with async_session_factory() as session:
            headphones_to_delete = await session.get(ShopItem, headphones_id)
            if headphones_to_delete:
                await session.delete(headphones_to_delete)
                await session.commit()

    @staticmethod
    async def select_all_shopitem():
        async_engine.echo = False
        async with async_session_factory() as session:
            query = select(ShopItem)
            result = await session.execute(query)
            objects = result.scalars().all()
            print(f"{objects=}")

    @staticmethod
    async def add_shopitem_into_cartitems(headphones_id, cart_id, quantity):
        async_engine.echo = False
        async with async_session_factory() as session:
            cart_item = CartItem(shopitem_id=headphones_id, cart_id=cart_id, quantity=quantity)
            session.add(cart_item)
            await session.commit()

    @staticmethod
    async def create_user(username, email, password):
        async_engine.echo = False
        async with async_session_factory() as session:
            user = User(username=username, email=email, password=password)
            session.add(user)
            await session.commit()

    @staticmethod
    async def create_cart(user_id):
        async_engine.echo = False
        #card_id and user_id must be equal and user_id is unique. It create one-to-one connection
        async with async_session_factory() as session:
            cart = Cart(cart_id=user_id, user_id=user_id)
            session.add(cart)
            await session.commit()

    @staticmethod
    async def select_cartitems(cart_id):
        async_engine.echo = False
        async with async_session_factory() as session:
            c_i = aliased(CartItem)
            s_i = aliased(ShopItem)
            query = (
                select(c_i, s_i)
                .join(c_i, c_i.shopitem_id == s_i.shopitem_id)
            )
            result = await session.execute(query)
            cart_items = result.scalars().all()
            print(f"{cart_items=}")

    @staticmethod
    async def update_shopitem():
        async_engine.echo = False
        async with async_session_factory() as session:
            pass
