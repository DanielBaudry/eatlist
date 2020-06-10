from typing import List

from src.domain.recipe import Recipe, RecipeRepository
from src.domain.shopping_list import ShoppingListRepository


class GetAvailableRecipes:
    def __init__(self, recipe_repository: RecipeRepository, shopping_list_repository: ShoppingListRepository):
        self.recipe_repository = recipe_repository
        self.shopping_list_repository = shopping_list_repository

    def execute(self, user_id: int) -> List[Recipe]:
        shopping_list = self.shopping_list_repository.get_shopping_list(user_id=user_id)
        available_recipes = self.recipe_repository.get_recipes()
        return [recipe for recipe in available_recipes if
                recipe.available_with_items(shopping_list.items)]
