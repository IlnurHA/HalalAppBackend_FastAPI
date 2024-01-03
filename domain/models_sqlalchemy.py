from sqlalchemy import Column, Integer, String, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

from typing import List

from domain.enums import Permissiveness


class BaseModel(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class FoodAdditives(BaseModel):
    __tablename__ = "foodAdditives"

    name: Mapped[Text] = mapped_column()
    permissiveness: Mapped[Enum[Permissiveness]] = mapped_column()
    e_number: Mapped[Text] = mapped_column()
    description: Mapped[Text] = mapped_column(nullable=True)
    img_src: Mapped[Text] = mapped_column(nullable=True)
    source: Mapped[Text] = mapped_column(nullable=True)


class IngredientsInfo(BaseModel):
    __tablename__ = "ingredientsInfo"

    name: Mapped[Text] = mapped_column()
    permissiveness: Mapped[Enum[Permissiveness]] = mapped_column()
    description: Mapped[Text] = mapped_column()
    img_src: Mapped[Text] = mapped_column(nullable=True)


class FederationEntity(BaseModel):
    __tablename__ = "federationEntities"

    name: Mapped[Text] = mapped_column()

    districts: Mapped[List["DistrictEntity"]] = relationship(back_populates="federation_entity")


class DistrictEntity(BaseModel):
    __tablename__ = "districtEntities"

    name: Mapped[Text] = mapped_column()
    federation_entity_fk: Mapped[int] = mapped_column(ForeignKey("FederationEntity.id", ondelete="CASCADE"))

    federation_entity: Mapped["FederationEntity"] = relationship(back_populates="districts")
    settlements: Mapped[List["DistrictSettlementEntity"]] = relationship(back_populates="district_entity")


class DistrictSettlementEntity(BaseModel):
    __tablename__ = "districtSettlementEntities"

    name: Mapped[Text] = mapped_column()
    district_entity_fk: Mapped[int] = mapped_column(ForeignKey("DistrictEntity.id", ondelete="CASCADE"))

    district_entity: Mapped["DistrictEntity"] = relationship(back_populates="settlements")
