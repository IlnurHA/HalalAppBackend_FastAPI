from typing import Any

from pydantic import BaseModel, Field, AnyUrl
from abc import ABC, abstractmethod

from domain.enums import Permissiveness
import domain.models_sqlalchemy as sql_models


class FromSQLModel(ABC):
    @classmethod
    @abstractmethod
    def fromSQLModel(cls, obj: Any) -> Any:
        pass


class FoodAdditive(BaseModel, FromSQLModel):
    food_additive_id: int = Field(..., alias="id", ge=0)
    name: str
    permissiveness: Permissiveness
    e_number: str
    description: str
    img_src: AnyUrl | None = Field(None)
    source: AnyUrl | None = Field(None)

    @classmethod
    def fromSQLModel(cls, obj: sql_models.FoodAdditive):
        return cls(
            id=obj.id,
            name=obj.name,
            permissiveness=obj.permissiveness,
            e_number=obj.e_number,
            description=obj.description,
            img_src=obj.img_src,
            source=obj.source
        )


class IngredientInfo(BaseModel, FromSQLModel):
    ingredient_info_id: int = Field(..., alias="id", ge=0)
    name: str
    permissiveness: Permissiveness
    description: str
    img_src: AnyUrl | None = Field(None)

    @classmethod
    def fromSQLModel(cls, obj: sql_models.IngredientsInfo):
        return cls(
            id=obj.id,
            name=obj.name,
            permissiveness=obj.permissiveness,
            description=obj.description,
            img_src=obj.img_src
        )
