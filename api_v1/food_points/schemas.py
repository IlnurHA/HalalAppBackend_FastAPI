from pydantic import BaseModel, AnyUrl, ConfigDict
from datetime import date

from domain.enums import FoodPointTypes, CuisineTypes


class FoodPointBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    is_prayer_room_exists: bool
    food_point_type: FoodPointTypes
    cuisine_type: CuisineTypes

    street: str
    building: str
    halal_certificate_expiration_date: date
    img_src: AnyUrl | None

    federation_name: str
    district_name: str
    district_settlement_name: str


class FoodPointCreate(FoodPointBase):
    pass


class FoodPoint(FoodPointBase):
    id: int


class FoodPointPatch(BaseModel):
    name: str | None = None
    is_prayer_room_exists: bool | None = None
    food_point_type: FoodPointTypes | None = None
    cuisine_type: CuisineTypes | None = None

    street: str | None = None
    building: str | None = None
    halal_certificate_expiration_date: date | None = None
    img_src: AnyUrl | None = None

    federation_name: str | None = None
    district_name: str | None = None
    district_settlement_name: str | None = None
