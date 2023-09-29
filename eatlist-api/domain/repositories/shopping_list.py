from abc import ABC, abstractmethod

from domain.entities.meal import MealForShoppingList
from domain.entities.shopping_list import ShoppingListBase


class ShoppingListRepo(ABC):
    @abstractmethod
    def create(self) -> ShoppingListBase:
        pass

    @abstractmethod
    def add_meal(self, shopping_list_id: int, meal: MealForShoppingList):
        pass
