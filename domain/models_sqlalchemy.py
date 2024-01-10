from sqlalchemy import ForeignKey, Enum, Date
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData

from typing import List

from domain.enums import Permissiveness, FoodPointTypes, CuisineTypes

metadata = MetaData()


class BaseModel(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


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


class FederationEntity(BaseModel):
    __tablename__ = "federationEntities"

    name: Mapped[str] = mapped_column()


class DistrictEntity(BaseModel):
    __tablename__ = "districtEntities"

    name: Mapped[str] = mapped_column()
    federation_fk: Mapped[int] = mapped_column(ForeignKey("federationEntities.id", ondelete="CASCADE"))

    federation_entity: Mapped["FederationEntity"] = relationship(lazy=False)


class DistrictSettlementEntity(BaseModel):
    __tablename__ = "districtSettlementEntities"

    name: Mapped[str] = mapped_column()
    district_fk: Mapped[str] = mapped_column(ForeignKey("districtEntities.id", ondelete="CASCADE"))

    district_entity: Mapped["DistrictEntity"] = relationship(lazy=False)


class FoodPoint(BaseModel):
    __tablename__ = "foodPoints"

    name: Mapped[str] = mapped_column()
    is_prayer_room_exists: Mapped[bool] = mapped_column()
    food_point_type = mapped_column(Enum(FoodPointTypes), nullable=False)
    cuisine_type = mapped_column(Enum(CuisineTypes), nullable=False)

    district_settlement_fk: Mapped[str] = mapped_column(
        ForeignKey("districtSettlementEntities.id", ondelete="CASCADE"))
    street: Mapped[str] = mapped_column()
    building: Mapped[str] = mapped_column()
    halal_certificate_expiration_date = mapped_column(Date, nullable=False)
    img_src: Mapped[str] = mapped_column()

    district_settlement: Mapped["DistrictSettlementEntity"] = relationship(lazy=False)
