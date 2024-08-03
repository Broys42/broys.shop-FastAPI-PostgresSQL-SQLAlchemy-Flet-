from src.model.headphones import Headphones as Headphones_model
from src.database.orm import async_orm
from src.database.database import Headphones as Headphones_db
from src.model.model import Model
import asyncio


class HeadphonesViewModel():
    def __init__(self, model: Model):
        self.model = model

    async def get_all_headphones(self) -> list[Headphones_model]:
        headphones_from_db : list[Headphones_db] = await async_orm.select_all_headphones()
        self.clear_headphones_model()
        for i in headphones_from_db:
            self.model.headphones.headphones.append(
                Headphones_model(
                    i.headphones_id, i.name, i.price, i.description, i.image,
                )
            )
        return self.model.headphones.headphones

    def clear_headphones_model(self):
        self.model.headphones.headphones.clear()
