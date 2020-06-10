from src.domain.shopping_list import ShoppingListRepository


class ArchiveCurrentShoppingList:
    def __init__(self, shopping_list_repository: ShoppingListRepository):
        self.shopping_list_repository = shopping_list_repository

    def execute(self, user_id: int) -> None:
        self.shopping_list_repository.archive_current_list(user_id)
