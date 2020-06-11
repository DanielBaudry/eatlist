from sqlalchemy import Column, String, Integer, Boolean, ARRAY

from src.infrastructure.database.models.model import Model


class ItemSQLEntity(Model):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(80), unique=True)

    seasonal_calendar = Column(ARRAY(Boolean), nullable=True)

    def __str__(self) -> str:
        return self.name
