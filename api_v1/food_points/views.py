from typing import List

from fastapi import APIRouter, Depends, Query, Path, Body, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from adapters import repository_instance
from domain.models_sqlalchemy import User

from . import crud
from .schemas import FoodPointCreate, FoodPoint
from ..auth import get_current_active_user

router = APIRouter(tags=['FoodPoints'])


@router.get('/', response_model=list[FoodPoint])
async def get_food_points(session: AsyncSession = Depends(repository_instance.session_dependency),
                          limit: int = Query(100), offset: int = Query(0)):
    return await crud.get_food_points(session=session, limit=limit, offset=offset)


@router.get('/{food_point_id}', response_model=FoodPoint)
async def get_food_point(session: AsyncSession = Depends(repository_instance.session_dependency),
                         food_point_id: int = Path(..., title="Food point id")):
    food_point = await crud.get_food_points_by_id(session=session, food_point_id=food_point_id)

    if food_point:
        return food_point

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Food point with id {food_point_id} not found")


@router.post('/', response_model=FoodPoint)
async def create_food_point(session: AsyncSession = Depends(repository_instance.session_dependency),
                            food_point_create: FoodPointCreate = Body(..., title="Food point create class"),
                            _: User = Depends(get_current_active_user)):
    return await crud.create_food_point(session=session, food_point=food_point_create)


@router.delete('/{food_point_id}')
async def delete_food_point(session: AsyncSession = Depends(repository_instance.session_dependency),
                            food_point_id: int = Path(..., title="Food point"),
                            _: User = Depends(get_current_active_user)):
    result = await crud.delete_food_point(session, food_point_id)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Food point with id {food_point_id} not found")
    return {"success": True}
