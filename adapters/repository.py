from typing import List, Tuple

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import select, insert, update, Result

from domain.models_sqlalchemy import FoodAdditive
from config import settings

from abc import ABC, abstractmethod


class BaseRepository(ABC):

    def __init__(self, db_url: str, db_echo: bool = False):
        self.engine = create_async_engine(
            url=db_url,
            echo=db_echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    @abstractmethod
    async def get_all(self, limit: int = 100, offset: int = 0):
        pass

    @abstractmethod
    async def get_by_id(self, id):
        pass

    @abstractmethod
    async def add(self, item):
        pass

    @abstractmethod
    async def update(self, item):
        pass

    @abstractmethod
    async def delete(self, item):
        pass


class FoodAdditivesRepository(BaseRepository):
    def __init__(self, db_url: str, db_echo: bool = False):
        super().__init__(db_url, db_echo)

    async def get_all(self, limit: int = 100, offset: int = 0) -> Result[tuple[FoodAdditive]]:
        async with self.session_factory() as session:
            result = await session.execute(select(FoodAdditive).offset(offset).limit(limit))
        return result

    async def get_by_id(self, id) -> Result[tuple[FoodAdditive]]:
        async with self.session_factory() as session:
            result = await session.execute(select(FoodAdditive).where(FoodAdditive.id == id))
        return result

    async def add(self, item: FoodAdditive):
        async with self.session_factory() as session:
            session.add(item)
            await session.commit()

    async def update(self, item: FoodAdditive):
        async with self.session_factory() as session:
            result = await session.execute(update(FoodAdditive).values(**item))
            await session.commit()

    async def delete(self, item: FoodAdditive):
        async with self.session_factory() as session:
            result = await session.delete(item)
            await session.commit()


food_additive_repository = FoodAdditivesRepository(settings.db_url)
