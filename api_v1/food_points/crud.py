from typing import List

from fastapi import HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from sqlalchemy.engine import Result

from domain.models_sqlalchemy import FoodPoint, DistrictSettlementEntity, DistrictEntity, FederationEntity
from .schemas import FoodPointCreate, FoodPoint as PydanticFoodPoint


def function_get_necessary_attributes(food_point: FoodPoint | None):
    if food_point is None:
        return None

    district_settlement: DistrictSettlementEntity = food_point.district_settlement
    district_entity: DistrictEntity = district_settlement.district_entity
    federation_entity: FederationEntity = district_entity.federation_entity

    food_point.federation_name = federation_entity.name
    food_point.district_name = district_entity.name
    food_point.district_settlement_name = district_settlement.name

    return food_point


async def create_food_point_helper(food_point: FoodPointCreate, session: AsyncSession) -> FoodPoint:
    statement = select(FederationEntity).where(FederationEntity.name == food_point.federation_name)
    result: Result = await session.execute(statement)
    federation_sql: FederationEntity = result.scalar_one_or_none()

    if not federation_sql:
        federation_sql = FederationEntity(name=food_point.federation_name)

        session.add(federation_sql)
        await session.commit()
        await session.refresh(federation_sql)

    statement = select(DistrictEntity).where(DistrictEntity.federation_fk == federation_sql.id)
    result: Result = await session.execute(statement)
    district_sql: DistrictEntity = result.scalar_one_or_none()

    if not district_sql:
        district_sql = DistrictEntity(name=food_point.district_name, federation_fk=federation_sql.id)
        session.add(district_sql)
        await session.commit()
        await session.refresh(district_sql)

    statement = select(DistrictSettlementEntity).where(DistrictSettlementEntity.district_fk == district_sql.id)
    result: Result = await session.execute(statement)
    district_settlement_sql: DistrictSettlementEntity = result.scalar_one_or_none()

    if not district_settlement_sql:
        district_settlement_sql = DistrictSettlementEntity(name=food_point.district_settlement_name,
                                                           district_fk=district_sql.id)
        session.add(district_settlement_sql)
        await session.commit()
        await session.refresh(district_settlement_sql)

    food_point_sql: FoodPoint = FoodPoint(district_settlement_fk=district_settlement_sql.id,
                                          name=food_point.name,
                                          is_prayer_room_exists=food_point.is_prayer_room_exists,
                                          food_point_type=food_point.food_point_type,
                                          cuisine_type=food_point.cuisine_type,
                                          street=food_point.street,
                                          building=food_point.building,
                                          halal_certificate_expiration_date=food_point.halal_certificate_expiration_date,
                                          img_src=food_point.img_src.unicode_string() if food_point.img_src else None)

    session.add(food_point_sql)
    await session.commit()
    await session.refresh(food_point_sql)

    return food_point_sql


async def get_food_points(session: AsyncSession,
                          limit: int = 100,
                          offset: int = 0) -> List[FoodPoint]:
    statement = select(FoodPoint).order_by(FoodPoint.id).limit(limit).offset(offset)
    result: Result = await session.execute(statement)

    food_points: List[FoodPoint] = list(map(function_get_necessary_attributes, result.scalars().all()))

    return food_points


async def get_food_points_by_id(session: AsyncSession,
                                food_point_id: int) -> FoodPoint | None:
    statement = select(FoodPoint).where(FoodPoint.id == food_point_id)
    result: Result = await session.execute(statement)

    food_point: FoodPoint | None = result.scalars().one_or_none()

    return function_get_necessary_attributes(food_point)


async def create_food_point(session: AsyncSession, food_point: FoodPointCreate) -> FoodPoint:
    food_point_sql: FoodPoint = await create_food_point_helper(session=session, food_point=food_point)

    return function_get_necessary_attributes(food_point_sql)


async def delete_food_point(session: AsyncSession, food_point_id: int):
    statement = delete(FoodPoint).where(FoodPoint.id == food_point_id).returning(FoodPoint)
    result: Result = await session.execute(statement)

    food_point: FoodPoint | None = result.scalars().one_or_none()

    await session.commit()

    return food_point
