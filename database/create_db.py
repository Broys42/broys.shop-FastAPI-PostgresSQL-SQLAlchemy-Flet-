if __name__ == "__main__":
    from database.orm import AsyncORM
    import asyncio
    async def main():
        async_orm = AsyncORM()
        await async_orm.create_tables()

    asyncio.run(main())
