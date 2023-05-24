from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


class DonationBase(BaseModel):
    full_amount: Optional[PositiveInt] = Field(None)
    comment: Optional[str] = Field(None, min_length=1)


class DonationCreate(DonationBase):
    full_amount: PositiveInt = Field(...)
    comment: Optional[str] = Field(None, min_length=1)


class DonationDB(DonationCreate):
    id: int
    create_date: datetime
    user_id: int
    invested_amount: int = Field(0)
    fully_invested: bool = Field(False)
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class DonationShortDB(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True
