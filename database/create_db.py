if __name__ == "__main__":
    from database.orm import AsyncORM
    import asyncio
    async def main():
        async_orm = AsyncORM()
        await async_orm.create_tables()
        await async_orm.insert_headphones(name="Кукусики", price=123, description="ЫВЫ", stock_quantity=4)
        await async_orm.insert_headphones(name="ЫФВЫФВ", price=123, description="ВАПАВ", stock_quantity=5)
        # await async_orm.delete_headphones(headphones_id=1)
        # await async_orm.select_all_shopitem()
        await async_orm.create_user(username="Шпеп", email="Шпеп", password="Шпе")
        await async_orm.create_cart(1)
        await async_orm.add_shopitem_into_cartitems(headphones_id=1, cart_id=1, quantity=3)
        # await async_orm.select_cartitems(1)
        await async_orm.delete_headphones(1)

    asyncio.run(main())
