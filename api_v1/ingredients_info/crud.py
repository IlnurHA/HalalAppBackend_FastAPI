from typing import List

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select, delete, update

from api_v1.ingredients_info.schemas import IngredientsInfoCreate, IngredientsInfoPatch
from domain.models_sqlalchemy import IngredientsInfo
from service.tools import update_url


async def get_ingredients_info(
        session: AsyncSession,
        limit: int = 100,
        offset: int = 0,
) -> List[IngredientsInfo]:
    statement = (select(IngredientsInfo)
                 .order_by(IngredientsInfo.id)
                 .limit(limit)
                 .offset(offset))

    result: Result = await session.execute(statement)

    ingredients = result.scalars().all()

    return list(ingredients)


async def get_ingredients_info_by_id(session: AsyncSession, ingredient_id: int) -> IngredientsInfo:
    statement = (select(IngredientsInfo)
                 .where(IngredientsInfo.id == ingredient_id))

    result: Result = await session.execute(statement)

    ingredient: IngredientsInfo = result.scalars().one_or_none()

    if ingredient:
        return ingredient

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Ingredient with id {ingredient_id} not found")


async def create_ingredient(session: AsyncSession, ingredients_info_create: IngredientsInfoCreate) -> IngredientsInfo:
    ingredients_info: IngredientsInfo = IngredientsInfo(**update_url(ingredients_info_create.model_dump()))
    session.add(ingredients_info)
    await session.commit()
    await session.refresh(ingredients_info)

    return ingredients_info


async def delete_ingredient(session: AsyncSession, ingredient_id: int):
    statement = (delete(IngredientsInfo)
                 .where(IngredientsInfo.id == ingredient_id)
                 .returning(IngredientsInfo))
    result = await session.execute(statement)

    ingredient: IngredientsInfo | None = result.scalar_one_or_none()

    await session.commit()

    return ingredient


async def patch_ingredient(session: AsyncSession, ingredient_id: int, ingredient_patch: IngredientsInfoPatch):
    statement = (update(IngredientsInfo)
                 .where(IngredientsInfo.id == ingredient_id)
                 .values(**ingredient_patch.model_dump(exclude_none=True))
                 .returning(IngredientsInfo))
    result = await session.execute(statement)

    ingredient: IngredientsInfo | None = result.scalar_one_or_none()

    await session.commit()
    if ingredient:
        await session.refresh(ingredient)

    return ingredient
