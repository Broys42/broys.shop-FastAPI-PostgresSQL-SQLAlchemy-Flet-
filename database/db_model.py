from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, Text, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from database.database import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    cart = relationship("Cart", uselist=False, back_populates="user", cascade="delete")

class ShopItem(Base):
    __tablename__ = 'shopitems'
    shopitem_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    description = Column(Text)
    stock_quantity = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    cart_items = relationship("CartItem", back_populates="shopitem", cascade="delete")

class Cart(Base):
    __tablename__ = 'carts'
    cart_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False, unique=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="cart")
    cart_items = relationship("CartItem", back_populates="cart", cascade="delete")

class CartItem(Base):
    __tablename__ = 'cartitems'
    cart_item_id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('carts.cart_id'), nullable=False)
    shopitem_id = Column(Integer, ForeignKey('shopitems.shopitem_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    cart = relationship("Cart", back_populates="cart_items")
    shopitem = relationship("ShopItem", back_populates="cart_items")
