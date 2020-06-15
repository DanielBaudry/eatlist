from datetime import datetime
from typing import Optional

from src.domain.item import Item


class ShoppingListItem(Item):
    def __init__(self, shopping_item_id: int = 0, shopping_date: Optional[datetime] = None, **kwargs):
        super().__init__(**kwargs)
        self.shopping_date = shopping_date
        self.shopping_item_id = shopping_item_id
