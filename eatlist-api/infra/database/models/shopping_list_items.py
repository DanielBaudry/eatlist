from typing import Optional

from sqlmodel import SQLModel, Field


class ShoppingListItems(SQLModel, table=True):
    shoplist_id: Optional[int] = Field(default=None, foreign_key="shoplist.id", primary_key=True)

    item_id: Optional[int] = Field(default=None, foreign_key="item.id", primary_key=True)
