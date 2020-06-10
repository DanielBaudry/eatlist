from src.domain.recipe import RecipeRepository
from src.domain.shopping_list import ShoppingListRepository


class AddAllRecipeItemsToShoppingList:
    def __init__(self, shopping_list_repository: ShoppingListRepository, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository
        self.shopping_list_repository = shopping_list_repository

    def execute(self, user_id: int, recipe_id: int) -> None:
        recipe = self.recipe_repository.get_recipe(recipe_id)
        self.shopping_list_repository.add_items(user_id, recipe.items)