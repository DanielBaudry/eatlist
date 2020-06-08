from sqlalchemy import Column, Integer, ForeignKey

from src.infrastructure.database.models.model import Model


class UserItemSQLEntity(Model):
    __tablename__ = 'user_item'

    id = Column(Integer, primary_key=True, autoincrement=True)

    userId = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)

    itemId = Column(Integer, ForeignKey("item.id"), nullable=False, index=True)
