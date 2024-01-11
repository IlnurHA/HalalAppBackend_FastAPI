from pydantic import BaseModel, AnyUrl, Field

from domain.enums import Permissiveness


class IngredientsInfoBase(BaseModel):
    name: str
    permissiveness: Permissiveness
    description: str | None = None
    img_src: AnyUrl | None = None


class IngredientsInfoCreate(IngredientsInfoBase):
    pass


class IngredientsInfo(IngredientsInfoBase):
    id: int


class IngredientsInfoPut(IngredientsInfoBase):
    pass


class IngredientsInfoPatch(BaseModel):
    name: str | None = None
    permissiveness: Permissiveness | None = None
    description: str | None = None
    img_src: AnyUrl | None = None
