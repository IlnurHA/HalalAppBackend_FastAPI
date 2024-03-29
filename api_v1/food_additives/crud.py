from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select, delete, update

from api_v1.food_additives.schemas import FoodAdditiveCreate, FoodAdditivesPatch
from domain.models_sqlalchemy import FoodAdditive
from service.tools import update_url


async def get_food_additives(session: AsyncSession, limit: int = 100, offset: int = 0) -> List[FoodAdditive]:
    statement = select(FoodAdditive).order_by(FoodAdditive.id).limit(limit).offset(offset)
    result: Result = await session.execute(statement)
    food_additive = result.scalars().all()
    return list(food_additive)


async def get_food_additive_by_id(session: AsyncSession, food_additive_id: int) -> FoodAdditive | None:
    statement = select(FoodAdditive).where(FoodAdditive.id == food_additive_id)
    result: Result = await session.execute(statement)
    food_additive = result.scalars().one_or_none()
    return food_additive


async def create_food_additive(session: AsyncSession, food_additive_create: FoodAdditiveCreate) -> FoodAdditive:
    food_additive = FoodAdditive(**update_url(food_additive_create.model_dump()))
    session.add(food_additive)
    await session.commit()
    await session.refresh(food_additive)

    return food_additive


async def delete_food_additive(session: AsyncSession, food_additive_id: int):
    statement = delete(FoodAdditive).where(FoodAdditive.id == food_additive_id).returning(FoodAdditive)
    result: Result = await session.execute(statement)

    food_additive: FoodAdditive | None = result.scalar_one_or_none()

    await session.commit()

    return food_additive


async def patch_food_additive(session: AsyncSession, food_additive_id: int,
                              food_additive_patch: FoodAdditivesPatch):
    statement = (update(FoodAdditive)
                 .where(FoodAdditive.id == food_additive_id)
                 .values(**food_additive_patch.model_dump(exclude_none=True))
                 .returning(FoodAdditive))
    result: Result = await session.execute(statement)

    food_additive: FoodAdditive | None = result.scalar_one_or_none()

    await session.commit()
    if food_additive:
        await session.refresh(food_additive)

    return food_additive
