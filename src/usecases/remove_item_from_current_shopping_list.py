from src.domain.shopping_list import ShoppingListRepository, ShoppingList


class RemoveItemFromCurrentShoppingList:
    def __init__(self, shopping_list_repository: ShoppingListRepository):
        self.shopping_list_repository = shopping_list_repository

    def execute(self, user_id: int, user_item_id: int) -> ShoppingList:
        return self.shopping_list_repository.remove_item(user_id, user_item_id)
