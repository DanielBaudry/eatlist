from src.domain.item import ItemRepository
from src.domain.shopping_list import ShoppingListRepository, ShoppingList


class AddItemToCurrentList:
    def __init__(self,
                 item_repository: ItemRepository,
                 shopping_list_repository: ShoppingListRepository):
        self.item_repository = item_repository
        self.shopping_list_repository = shopping_list_repository

    def execute(self, new_item_name: str, user_id: int) -> ShoppingList:
        item = self.item_repository.convert_item_from_name(new_item_name)
        return self.shopping_list_repository.add_item(item, user_id)
