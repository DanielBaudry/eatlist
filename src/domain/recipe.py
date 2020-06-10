from abc import abstractmethod, ABC
from typing import List

from src.domain.item import Item


class Recipe:
    def __init__(self, identifier: int, name: str, items: List[Item] = []):
        self.identifier = identifier
        self.name = name
        self.items = items

    def available_with_items(self, items: List[Item]) -> bool:
        if set(self.items).issubset(items):
            return True
        return False


class RecipeRepository(ABC):
    @abstractmethod
    def get_recipes(self) -> List[Recipe]:
        pass

    @abstractmethod
    def get_recipe(self, recipe_id: int) -> Recipe:
        pass
