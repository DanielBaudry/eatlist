from typing import Optional

from sqlmodel import Field, Relationship

from domain.entities.item import ItemBase
from infra.database.models.meal_sql import MealSQL
from infra.database.models.shopping_list import ShoppingListSQL


class Item(ItemBase, table=True):
    __tablename__: str = "item"

    id: Optional[int] = Field(default=None, primary_key=True)

    meal_id: Optional[int] = Field(default=None, foreign_key="meal.id")

    meal: Optional[MealSQL] = Relationship(back_populates="items")

    shoplist_id: Optional[int] = Field(default=None, foreign_key="shoplist.id")

    shoplist: Optional[ShoppingListSQL] = Relationship(back_populates="items")
