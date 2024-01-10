from fastapi import APIRouter, Depends, Body, Path
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.ingredients_info import crud
from adapters.repository import repository_instance
from .schemas import IngredientsInfo, IngredientsInfoCreate

router = APIRouter(tags=['IngredientsInfo'])


@router.get('/')
async def get_ingredients_info(session: AsyncSession = Depends(repository_instance.session_dependency),
                               limit: int = 100, offset: int = 0):
    return await crud.get_ingredients_info(session=session, limit=limit, offset=offset)


@router.get('/{ingredient_id}')
async def get_ingredients_info_by_id(session: AsyncSession = Depends(repository_instance.session_dependency),
                                     ingredient_id: int = Path(..., title="Ingredient ID")):
    return await crud.get_ingredients_info_by_id(session=session, ingredient_id=ingredient_id)


@router.post('/')
async def create_ingredient(session: AsyncSession = Depends(repository_instance.session_dependency),
                            ingredient_create: IngredientsInfoCreate = Body(...)) -> IngredientsInfo:
    return await crud.create_ingredient(session=session, ingredients_info_create=ingredient_create)
