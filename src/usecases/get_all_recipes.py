from typing import List

from src.domain.recipe import RecipeRepository, Recipe


class GetAllRecipes:    
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository
        
    def execute(self) -> List[Recipe]:
        return self.recipe_repository.get_recipes()
