from sqlalchemy import Column, String, Integer

from src.infrastructure.database.models.model import Model


class ItemSQLEntity(Model):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(80), unique=True)
