from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.infrastructure.database.models.db import db
from src.infrastructure.database.models.model import Model


class RecipeSQLEntity(Model):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(80), unique=True)

    items = relationship('ItemSQLEntity',
                         backref=db.backref('item', lazy='dynamic'),
                         secondary='recipe_item')
