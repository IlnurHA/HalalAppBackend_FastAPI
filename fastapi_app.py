from fastapi import FastAPI, Query
from adapters.repository import food_additive_repository
from domain.models_pydantic import FoodAdditive
from service.tools import to_db_class

app = FastAPI()


@app.get("/api/v2/food_additives")
def get_food_additives(limit: int = Query(100, ge=0), offset: int = Query(0, ge=0)):
    return food_additive_repository.get_all(limit=limit, offset=offset)


@app.get("/api/v2/food_additives/{food_additive_id}")
def get_food_additive(food_additive_id: int):
    return food_additive_repository.get_by_id(food_additive_id)


# @app.post("/api/v2/food_additives")
# def add_new_food_additive(food_additive: FoodAdditive):
#     return food_additive_repository.add(to_db_class(food_additive))
#
#
# @app.put("/api/v2/food_additives/{food_additive_id}")
# def update_food_additive(food_additive_id: int, food_additive: FoodAdditive):
#     food_additive.id = food_additive_id
#     return food_additive_repository.update(to_db_class(food_additive))
