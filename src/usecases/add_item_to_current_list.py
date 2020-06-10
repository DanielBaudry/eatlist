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
        shopping_list = self.shopping_list_repository.get_shopping_list(user_id)

        shopping_list.add_item(item)

        return self.shopping_list_repository.update(shopping_list)
