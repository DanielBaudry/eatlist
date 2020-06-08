from src.domain.shopping_list import ShoppingListRepository, ShoppingList


class GetCurrentShoppingList:
    def __init__(self, shopping_list_repository: ShoppingListRepository):
        self.shopping_list_repository = shopping_list_repository

    def execute(self, user_id: int) -> ShoppingList:
        return self.shopping_list_repository.get_current_list(user_id)
