from typing import Optional, List
from sqlmodel import Field, Relationship

from domain.entities.shopping_list import ShoppingListBase
from infra.database.models.shopping_list_items import ShoppingListItems


class ShoppingListSQL(ShoppingListBase, table=True):
    __tablename__: str = "shoplist"

    id: Optional[int] = Field(default=None, primary_key=True)

    items: List["Item"] = Relationship(back_populates="shoplists", link_model=ShoppingListItems)
