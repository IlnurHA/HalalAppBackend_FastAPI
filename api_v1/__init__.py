from fastapi import APIRouter

from .food_additives import router as food_additive_router

router = APIRouter()
router.include_router(router=food_additive_router, prefix="/food_additives")
