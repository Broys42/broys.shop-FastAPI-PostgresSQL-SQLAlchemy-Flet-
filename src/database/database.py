from config import settings
from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base, relationship, sessionmaker, Mapped, mapped_column
from sqlalchemy import Boolean, create_engine, Column, Integer, String, DECIMAL, Text, ForeignKey, TIMESTAMP, func

DATABASE_URL = settings.DATABASE_URL_asyncpg

class Base(DeclarativeBase):
    pass

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # For Fast-Api-Users (also email)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    cart = relationship("Cart", uselist=False, back_populates="user", cascade="delete")

class Headphones(Base):
    __tablename__ = 'headphones'
    headphones_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer(), nullable=False)
    description = Column(String(1000))
    image = Column(String(300), nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    cart_items = relationship("CartItem", back_populates="headphones", cascade="delete")

class Cart(Base):
    __tablename__ = 'carts'
    cart_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="cart")
    cart_items = relationship("CartItem", back_populates="cart", cascade="delete")

class CartItem(Base):
    __tablename__ = 'cartitems'
    cart_item_id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('carts.cart_id'), nullable=False)
    headphones_id = Column(Integer, ForeignKey('headphones.headphones_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    cart = relationship("Cart", back_populates="cart_items")
    headphones = relationship("Headphones", back_populates="cart_items")

async_engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
