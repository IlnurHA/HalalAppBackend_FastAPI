from pydantic import BaseModel, AnyUrl, Field, ConfigDict

from domain.enums import Permissiveness


class FoodAdditiveBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    permissiveness: Permissiveness
    e_number: str
    description: str | None = None
    img_src: AnyUrl | None = None
    source: AnyUrl | None = None


class FoodAdditiveCreate(FoodAdditiveBase):
    pass


class FoodAdditive(FoodAdditiveBase):
    id: int


class FoodAdditivesPatch(BaseModel):
    name: str | None = None
    permissiveness: Permissiveness | None = None
    e_number: str | None = None
    description: str | None = None
    img_src: AnyUrl | None = None
    source: AnyUrl | None = None
