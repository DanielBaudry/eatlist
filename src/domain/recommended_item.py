from datetime import datetime, timedelta

from src.domain.shopping_list_item import ShoppingListItem


class RecommendedItem(ShoppingListItem):
    def __init__(self, score: int = 0, **kwargs):
        super().__init__(**kwargs)
        self.score = score

    def compute_score(self) -> None:
        if self.shopping_date < datetime.now() + timedelta(days=7):
            self.score += 10
        if self.is_seasonal():
            self.score += 10
