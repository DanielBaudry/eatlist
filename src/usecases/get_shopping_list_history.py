from typing import List

from src.domain.shopping_list import ShoppingListRepository
from src.domain.shopping_list_history import ShoppingListHistory


class GetShoppingListHistory:
    def __init__(self, shopping_list_repository: ShoppingListRepository):
        self.shopping_list_repository = shopping_list_repository

    def execute(self, user_id: int) -> ShoppingListHistory:
        shopping_list_history = self.shopping_list_repository.get_history(user_id)
        return shopping_list_history

