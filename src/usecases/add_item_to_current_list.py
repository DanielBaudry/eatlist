from src.domain.item import ItemRepository
from src.domain.shopping_list import ShoppingListRepository, ShoppingList


class AddItemToCurrentList:
    def __init__(self,
                 item_repository: ItemRepository,
                 shopping_list_repository: ShoppingListRepository):
        self.item_repository = item_repository
        self.shopping_list_repository = shopping_list_repository

    def execute(self, new_item_name: str, user_id: int) -> ShoppingList:
        item = self.item_repository.add_item_to_referential(new_item_name)

        shopping_list = self.shopping_list_repository.get_current_list(user_id)

        if shopping_list.already_contains(item):
            return shopping_list

        return self.shopping_list_repository.add_item(item, user_id)
