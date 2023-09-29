from domain.entities.meal import MealBase, MealForShoppingList
from domain.entities.shopping_list import UpdateShoppingList
from domain.repositories.shopping_list import ShoppingListRepo


class AddMealToShoppingList:
    def __init__(self, shopping_list_repo: ShoppingListRepo):
        self.shopping_list_repo = shopping_list_repo

    def execute(self, shopping_list_id: int, meal: MealForShoppingList):
        return self.shopping_list_repo.add_meal(shopping_list_id, meal)
