from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

from pydantic import BaseModel, ConfigDict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .food_additives import router as food_additive_router
from .ingredients_info import router as ingredients_router
from .food_points import router as food_point_router
from .auth import router as auth_router

from adapters import repository_instance

router = APIRouter()
router.include_router(router=food_additive_router, prefix="/food_additives")
router.include_router(router=ingredients_router, prefix="/ingredients_info")
router.include_router(router=food_point_router, prefix="/food_points")
router.include_router(router=auth_router, prefix="/login")
