from fastapi import APIRouter, Depends
from src.database.orm import AsyncORM

asyncOrm = AsyncORM()

headphones_router = APIRouter(
    prefix="/Headphones",
    tags=["Headphones"]
)

@headphones_router.post("/add")
async def add_headphones(name: str, description: str, price: float, image: str, stock_quantity: int):
    try:
        await asyncOrm.insert_headphones(name=name, description=description, price=price, image=image, stock_quantity=stock_quantity)
    except Exception as e:
        return {"error" : e}
    else:
        return {"status" : "200"}

@headphones_router.post("/delete")
async def delete_headphones(id: int):
    try:
        await asyncOrm.delete_headphones(id)
    except Exception as e:
        return {"error" : e}
    else:
        return {"status" : "200"}

@headphones_router.post("/change_stock_quantity")
async def change_stock_quantity(id: int, stock_quantity: int):
    try:
        await asyncOrm.change_stock_quantity(id, stock_quantity)
    except Exception as e:
        return {"error" : e}
    else:
        return {"status" : "200"}

@headphones_router.post("/change_name")
async def change_name(id: int, name: str):
    try:
        await asyncOrm.change_heaphones_name(id, name)
    except Exception as e:
        return {"error" : e}
    else:
        return {"status" : "200"}

@headphones_router.get("/get_all_headphones")
async def get_all_headphones():
    try:
        await asyncOrm.change_heaphones_name()
    except Exception as e:
        return {"error" : e}
    else:
        return {"status" : "200"}
