from fastapi import FastAPI, Query
from adapters.repository import repository_instance
from domain.models_sqlalchemy import BaseModel, BaseForFoodPointSchema
from config import settings
from contextlib import asynccontextmanager

from api_v1 import router as api_v1_router


@asynccontextmanager
async def fast_api_lifespan(_: FastAPI):
    async with repository_instance.engine.begin() as connection:
        await connection.run_sync(BaseModel.metadata.create_all)
        await connection.run_sync(BaseForFoodPointSchema.metadata.create_all)
    yield


app = FastAPI(lifespan=fast_api_lifespan)
app.include_router(api_v1_router, prefix="/api/v1")
