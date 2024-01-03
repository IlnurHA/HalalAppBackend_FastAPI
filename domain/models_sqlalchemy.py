from sqlalchemy import Column, Integer, String, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

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
