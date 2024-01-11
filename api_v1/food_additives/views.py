from typing import List

from fastapi import APIRouter, HTTPException, status, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from adapters import repository_instance
from domain.models_sqlalchemy import User

from . import crud
from .schemas import FoodAdditive, FoodAdditiveCreate

from ..auth import get_current_active_user

router = APIRouter(tags=['FoodAdditives'])


@router.get("/", response_model=list[FoodAdditive])
async def get_food_additives(session: AsyncSession = Depends(repository_instance.session_dependency),
                             limit: int = 100, offset: int = 0):
    return await crud.get_food_additives(session, limit=limit, offset=offset)


@router.post("/", response_model=FoodAdditive)
async def create_food_additive(session: AsyncSession = Depends(repository_instance.session_dependency),
                               food_additive: FoodAdditiveCreate = Body(...),
                               user: User = Depends(get_current_active_user)):
    return await crud.create_food_additive(session, food_additive)


@router.get("/{food_additive_id}", response_model=FoodAdditive)
async def get_food_additive(food_additive_id: int,
                            session: AsyncSession = Depends(repository_instance.session_dependency)):
    food_additive = await crud.get_food_additive_by_id(session, food_additive_id)

    if food_additive:
        return food_additive

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Food additive with id {food_additive_id} not found")


@router.delete("/{food_additive_id}")
async def delete_food_additive(food_additive_id: int,
                               session: AsyncSession = Depends(repository_instance.session_dependency)):
    result = await crud.delete_food_additive(food_additive_id=food_additive_id, session=session)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Food additive with id {food_additive_id} not found")

    return {"success": True}
