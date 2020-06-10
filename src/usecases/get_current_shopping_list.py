from datetime import datetime
from typing import Optional

from src.domain.shopping_list import ShoppingListRepository, ShoppingList


class GetCurrentShoppingList:
    def __init__(self, shopping_list_repository: ShoppingListRepository):
        self.shopping_list_repository = shopping_list_repository

    def execute(self, user_id: int, shopping_list_date: Optional[datetime] = None) -> ShoppingList:
        return self.shopping_list_repository.get_shopping_list(user_id, shopping_list_date)
