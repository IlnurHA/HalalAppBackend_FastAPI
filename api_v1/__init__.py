from fastapi import APIRouter

from .food_additives import router as food_additive_router
from .ingredients_info import router as ingredients_router
from .food_points import router as food_point_router

router = APIRouter()
router.include_router(router=food_additive_router, prefix="/food_additives")
router.include_router(router=ingredients_router, prefix="/ingredients_info")
router.include_router(router=food_point_router, prefix="/food_points")
