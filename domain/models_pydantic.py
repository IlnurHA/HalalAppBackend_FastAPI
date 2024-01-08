from typing import Any

from pydantic import BaseModel, Field, AnyUrl
from abc import ABC, abstractmethod
from datetime import date

from domain.enums import Permissiveness, FoodPointTypes, CuisineTypes
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


class FoodPoint(BaseModel):
    food_point_id: int = Field(..., alias="id", ge=0)
    branch_name: str
    is_prayer_room_exist: bool
    food_point_type: FoodPointTypes
    cuisine_type: CuisineTypes
    street: str
    halal_certificate_expiration_date: date
    img_src: AnyUrl | None = Field(None)
    federation_name: str
    district_name: str
    district_settlement_name: str

    @classmethod
    def fromSQLModel(cls, food_point_sql_obj: sql_models.FoodPoint, federation_sql_obj: sql_models.FederationEntity,
                     district_sql_obj: sql_models.DistrictEntity,
                     district_settlement_sql_obj: sql_models.DistrictSettlementEntity):
        return cls(
            food_point_id=food_point_sql_obj.id,
            branch_name=food_point_sql_obj.name,
            is_prayer_room_exist=food_point_sql_obj.is_prayer_room_exists,
            food_point_type=food_point_sql_obj.food_point_type,
            cuisine_type=food_point_sql_obj.cuisine_type,
            street=food_point_sql_obj.street,
            halal_certificate_expiration_date=food_point_sql_obj.halal_certificate_expiration_date,
            img_src=food_point_sql_obj.img_src,
            federation_name=federation_sql_obj.name,
            district_name=district_sql_obj.name,
            district_settlement_name=district_settlement_sql_obj.name
        )
