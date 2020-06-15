from typing import List

from src.domain.recommended_item import RecommendedItem
from src.domain.shopping_list import ShoppingListRepository


class RecommendItems:
    def __init__(self, shopping_list_repository: ShoppingListRepository):
        self.shopping_list_repository = shopping_list_repository

    def execute(self, user_id: int) -> List[RecommendedItem]:
        recommended_items = self.shopping_list_repository.get_all_shopping_list(user_id)
        for item in recommended_items:
            item.compute_score()
        return sorted(recommended_items, key=lambda it: it.score, reverse=True)
