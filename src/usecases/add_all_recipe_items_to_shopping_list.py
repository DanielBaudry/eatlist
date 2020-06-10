from src.domain.recipe import RecipeRepository
from src.domain.shopping_list import ShoppingListRepository


class AddAllRecipeItemsToShoppingList:
    def __init__(self, shopping_list_repository: ShoppingListRepository, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository
        self.shopping_list_repository = shopping_list_repository

    def execute(self, user_id: int, recipe_id: int) -> None:
        recipe = self.recipe_repository.get_recipe(recipe_id)
        shopping_list = self.shopping_list_repository.get_shopping_list(user_id)
        shopping_list.add_items(recipe.items)
        self.shopping_list_repository.update(shopping_list)
