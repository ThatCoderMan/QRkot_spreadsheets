from sqlalchemy import Column, String, Text

from .base import BaseAbstractModel


class CharityProject(BaseAbstractModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return f'Charity project {self.name}'
