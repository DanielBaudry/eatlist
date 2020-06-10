from datetime import datetime
from typing import List


class ShoppingListHistory:
    def __init__(self, shopping_list_date: List[datetime]):
        self.shopping_list_date = shopping_list_date
