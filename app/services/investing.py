from datetime import datetime
from typing import List, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


async def get_not_closed_investing_objects(
        model: Union[CharityProject, Donation],
        session: AsyncSession
) -> List[Union[CharityProject, Donation]]:
    db_obj = await session.execute(
        select(model).where(
            model.fully_invested == 0
        ).order_by(model.create_date)
    )
    return db_obj.scalars().all()


def close_investing_object(
        obj_to_close: Union[CharityProject, Donation]
):
    obj_to_close.invested_amount = obj_to_close.full_amount
    obj_to_close.fully_invested = True
    obj_to_close.close_date = datetime.now()


def make_investing(
        new_obj: Union[CharityProject, Donation],
        model_obj: Union[CharityProject, Donation]
) -> (Union[CharityProject, Donation], Union[CharityProject, Donation]):
    new_obj_free_amount = new_obj.full_amount - new_obj.invested_amount
    model_obj_free_amount = model_obj.full_amount - model_obj.invested_amount
    if new_obj_free_amount == model_obj_free_amount:
        close_investing_object(new_obj)
        close_investing_object(model_obj)
    elif new_obj_free_amount > model_obj_free_amount:
        new_obj.invested_amount += model_obj_free_amount
        close_investing_object(model_obj)
    else:
        model_obj.invested_amount += new_obj_free_amount
        close_investing_object(new_obj)
    return new_obj, model_obj


async def investing_process(
        new_object: Union[CharityProject, Donation],
        model: Union[CharityProject, Donation],
        session: AsyncSession
):
    model_objects = await get_not_closed_investing_objects(model, session)
    for model_object in model_objects:
        new_obj, model_obj = make_investing(new_object, model_object)
        session.add(new_obj)
        session.add(model_obj)
    await session.commit()
    await session.refresh(new_object)
