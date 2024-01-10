from sqlalchemy import ForeignKey, Enum, Date
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData

from typing import List

from domain.enums import Permissiveness, FoodPointTypes, CuisineTypes

metadata = MetaData()


class BaseModel(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class BaseForFoodPointSchema(DeclarativeBase):
    __abstract__ = True


class FoodAdditive(BaseModel):
    __tablename__ = "foodAdditives"

    name: Mapped[str] = mapped_column()
    permissiveness: Mapped[Permissiveness] = mapped_column(Enum(Permissiveness), nullable=False)
    e_number: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(nullable=True)
    img_src: Mapped[str] = mapped_column(nullable=True)
    source: Mapped[str] = mapped_column(nullable=True)


class IngredientsInfo(BaseModel):
    __tablename__ = "ingredientsInfo"

    name: Mapped[str] = mapped_column()
    permissiveness = mapped_column(Enum(Permissiveness), nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    img_src: Mapped[str] = mapped_column(nullable=True)


class FederationEntity(BaseForFoodPointSchema):
    __tablename__ = "federationEntities"

    name: Mapped[str] = mapped_column(primary_key=True)


class DistrictEntity(BaseForFoodPointSchema):
    __tablename__ = "districtEntities"

    name: Mapped[str] = mapped_column(primary_key=True)
    federation_name: Mapped[str] = mapped_column(ForeignKey("federationEntities.name", ondelete="CASCADE"))

    federation_entity: Mapped["FederationEntity"] = relationship()


class DistrictSettlementEntity(BaseForFoodPointSchema):
    __tablename__ = "districtSettlementEntities"

    name: Mapped[str] = mapped_column(primary_key=True)
    district_name: Mapped[str] = mapped_column(ForeignKey("districtEntities.name", ondelete="CASCADE"))

    district_entity: Mapped["DistrictEntity"] = relationship()


class FoodPoint(BaseForFoodPointSchema):
    __tablename__ = "foodPoints"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column()
    is_prayer_room_exists: Mapped[bool] = mapped_column()
    food_point_type = mapped_column(Enum(FoodPointTypes), nullable=False)
    cuisine_type = mapped_column(Enum(CuisineTypes), nullable=False)

    district_settlement_name: Mapped[str] = mapped_column(
        ForeignKey("districtSettlementEntities.name", ondelete="CASCADE"))
    street: Mapped[str] = mapped_column()
    building: Mapped[str] = mapped_column()
    halal_certificate_expiration_date = mapped_column(Date, nullable=False)
    img_src: Mapped[str] = mapped_column()

    district_settlement: Mapped["DistrictSettlementEntity"] = relationship()
