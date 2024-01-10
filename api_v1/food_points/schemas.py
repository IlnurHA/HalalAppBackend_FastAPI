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
