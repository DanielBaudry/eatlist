from abc import ABC, abstractmethod

from domain.entities.shopping_list import ShoppingListBase


class ShoppingListRepo(ABC):
    @abstractmethod
    def create(self) -> ShoppingListBase:
        pass
