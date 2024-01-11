from fastapi import APIRouter, Depends, Body, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from adapters import repository_instance
from domain.models_sqlalchemy import User

from . import crud
from .schemas import IngredientsInfo, IngredientsInfoCreate
from ..auth import get_current_active_user

router = APIRouter(tags=['IngredientsInfo'])


@router.get('/', response_model=list[IngredientsInfo])
async def get_ingredients_info(session: AsyncSession = Depends(repository_instance.session_dependency),
                               limit: int = 100, offset: int = 0):
    return await crud.get_ingredients_info(session=session, limit=limit, offset=offset)


@router.get('/{ingredient_id}', response_model=IngredientsInfo)
async def get_ingredients_info_by_id(session: AsyncSession = Depends(repository_instance.session_dependency),
                                     ingredient_id: int = Path(..., title="Ingredient ID")):
    return await crud.get_ingredients_info_by_id(session=session, ingredient_id=ingredient_id)


@router.post('/', response_model=IngredientsInfo)
async def create_ingredient(session: AsyncSession = Depends(repository_instance.session_dependency),
                            ingredient_create: IngredientsInfoCreate = Body(...),
                            user: User = Depends(get_current_active_user)) -> IngredientsInfo:
    return await crud.create_ingredient(session=session, ingredients_info_create=ingredient_create)


@router.delete('/{ingredient_id}')
async def delete_ingredient(session: AsyncSession = Depends(repository_instance.session_dependency),
                            ingredient_id: int = Path(..., title="Ingredient"),
                            user: User = Depends(get_current_active_user)):
    result = await crud.delete_ingredient(session=session, ingredient_id=ingredient_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Food additive with id {ingredient_id} not found")
    return {"success": True}
