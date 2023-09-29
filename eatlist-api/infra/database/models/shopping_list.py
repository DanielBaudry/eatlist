from typing import Optional, List
from sqlmodel import Field, Relationship

from domain.entities.shopping_list import ShoppingListBase


class ShoppingListSQL(ShoppingListBase, table=True):
    __tablename__: str = "shoplist"

    id: Optional[int] = Field(default=None, primary_key=True)

    items: List["Item"] = Relationship(back_populates="shoplist")
