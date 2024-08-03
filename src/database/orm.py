from sqlalchemy import select, text, insert, func, cast
from sqlalchemy.orm import aliased
import asyncio
from src.database.database import Base, User, Headphones, Cart, CartItem, async_engine, async_session_maker

class AsyncORM():
    def __init__(self):
        pass

    @staticmethod
    async def create_db_and_tables():
        async_engine.echo = True
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        async_engine.echo = False

    @staticmethod
    async def insert_headphones(name, description, price, image, stock_quantity):
        async_engine.echo = True
        async with async_session_maker() as session:
            headphones = Headphones(name=name, description=description, price=price, image=image, stock_quantity=stock_quantity)
            session.add(headphones)
            await session.commit()
            async_engine.echo = False

    @staticmethod
    async def change_stock_quantity(id, stock_quantity):
        async_engine.echo = True
        async with async_session_maker() as session:
            headphones : Headphones = await session.get(Headphones, id)
            headphones.stock_quantity = stock_quantity
            await session.commit()

    @staticmethod
    async def change_heaphones_name(id, name):
        async_engine.echo = True
        async with async_session_maker() as session:
            headphones : Headphones = await session.get(Headphones, id)
            headphones.name = name
            await session.commit()

    @staticmethod
    async def delete_headphones(headphones_id):
        async with async_session_maker() as session:
            headphones_to_delete = await session.get(Headphones, headphones_id)
            if headphones_to_delete:
                await session.delete(headphones_to_delete)
                await session.commit()

    @staticmethod
    async def select_all_headphones():
        async_engine.echo = True
        async with async_session_maker() as session:
            query = select(Headphones)
            result = await session.execute(query)
            objects = result.scalars().all()
            # print(f"{objects=}")
            return objects

    @staticmethod
    async def add_headphones_into_cartitems(headphones_id, cart_id, quantity):
        async_engine.echo = False
        async with async_session_maker() as session:
            cart_item = CartItem(shopitem_id=headphones_id, cart_id=cart_id, quantity=quantity)
            session.add(cart_item)
            await session.commit()

    @staticmethod
    async def create_user(username, email, password):
        async_engine.echo = False
        async with async_session_maker() as session:
            user = User(username=username, email=email, password=password)
            session.add(user)
            await session.commit()

    @staticmethod
    async def create_cart(user_id):
        async_engine.echo = False
        #card_id and user_id must be equal and user_id is unique. It create one-to-one connection
        async with async_session_maker() as session:
            cart = Cart(cart_id=user_id, user_id=user_id)
            session.add(cart)
            await session.commit()

    @staticmethod
    async def select_cartitems(cart_id):
        async_engine.echo = False
        async with async_session_maker() as session:
            c_i = aliased(CartItem)
            s_i = aliased(Headphones)
            query = (
                select(c_i, s_i)
                .join(c_i, c_i.shopitem_id == s_i.headphones_id)
            )
            result = await session.execute(query)
            cart_items = result.scalars().all()
            print(f"{cart_items=}")

    @staticmethod
    async def update_shopitem():
        async_engine.echo = False
        async with async_session_maker() as session:
            pass

async_orm = AsyncORM()
