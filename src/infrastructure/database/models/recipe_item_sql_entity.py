import bcrypt
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, LargeBinary, ForeignKey

from src.infrastructure.database.models.model import Model


class RecipeItemSQLEntity(Model):
    __tablename__ = 'recipe_item'

    id = Column(Integer, primary_key=True, autoincrement=True)

    recipeId = Column(Integer, ForeignKey("recipe.id"), nullable=False, index=True)

    itemId = Column(Integer, ForeignKey("item.id"), nullable=False, index=True)
