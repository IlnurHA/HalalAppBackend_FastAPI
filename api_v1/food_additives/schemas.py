from pydantic import BaseModel, AnyUrl, Field, ConfigDict

from domain.enums import Permissiveness


class FoodAdditiveBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    permissiveness: Permissiveness
    e_number: str
    description: str | None
    img_src: AnyUrl | None
    source: AnyUrl | None


class FoodAdditiveCreate(FoodAdditiveBase):
    pass


class FoodAdditive(FoodAdditiveBase):
    id: int = Field(..., ge=0)
