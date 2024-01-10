from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Date
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData

from typing import List, Any
from abc import ABC, abstractmethod

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
    description: Mapped[str] = mapped_column()
    img_src: Mapped[str] = mapped_column(nullable=True)


class FederationEntity(BaseModel):
    __tablename__ = "federationEntities"

    name: Mapped[str] = mapped_column()

    districts: Mapped[List["DistrictEntity"]] = relationship(back_populates="federation_entity")


class DistrictEntity(BaseModel):
    __tablename__ = "districtEntities"

    name: Mapped[str] = mapped_column()
    federation_entity_fk: Mapped[int] = mapped_column(ForeignKey("federationEntities.id", ondelete="CASCADE"))

    federation_entity: Mapped["FederationEntity"] = relationship(back_populates="districts")
    settlements: Mapped[List["DistrictSettlementEntity"]] = relationship(back_populates="district_entity")


class DistrictSettlementEntity(BaseModel):
    __tablename__ = "districtSettlementEntities"

    name: Mapped[str] = mapped_column()
    district_entity_fk: Mapped[int] = mapped_column(ForeignKey("districtEntities.id", ondelete="CASCADE"))

    district_entity: Mapped["DistrictEntity"] = relationship(back_populates="settlements")

    food_points: Mapped[List["FoodPoint"]] = relationship(back_populates="district_settlement")


class FoodPoint(BaseModel):
    __tablename__ = "foodPoints"

    name: Mapped[str] = mapped_column()
    is_prayer_room_exists: Mapped[bool] = mapped_column()
    food_point_type = mapped_column(Enum(FoodPointTypes), nullable=False)
    cuisine_type = mapped_column(Enum(CuisineTypes), nullable=False)

    district_settlement_fk: Mapped[int] = mapped_column(ForeignKey("districtSettlementEntities.id", ondelete="CASCADE"))
    street: Mapped[str] = mapped_column()
    building: Mapped[str] = mapped_column()
    halal_certificate_expiration_date = mapped_column(Date, nullable=False)
    img_src: Mapped[str] = mapped_column()

    district_settlement: Mapped["DistrictSettlementEntity"] = relationship(back_populates="food_points")
