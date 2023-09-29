from domain.repositories.shopping_list import ShoppingListRepo


class CreateNewShoppingList:
    def __init__(self, shopping_list_repo: ShoppingListRepo):
        self.shopping_list_repo = shopping_list_repo

    def execute(self):
        return self.shopping_list_repo.create()
