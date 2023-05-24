from sqlalchemy import Column, ForeignKey, Integer, Text

from .base import BaseAbstractModel


class Donation(BaseAbstractModel):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    def __repr__(self):
        return f'Donation by {self.user_id}'
