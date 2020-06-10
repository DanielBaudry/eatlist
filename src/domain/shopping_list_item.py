from src.domain.item import Item


class ShoppingListItem(Item):
    def __init__(self, shopping_item_id: int = 0, **kwargs):
        super().__init__(**kwargs)
        self.shopping_item_id = shopping_item_id
