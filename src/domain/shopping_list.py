from abc import abstractmethod, ABC
from typing import List

from src.domain.item import Item


class ShoppingList:
    def __init__(self, user_id: int, items: List = []):
        self.user_id = user_id
        self.items = items

    def already_contains(self, new_item: Item) -> bool:
        for item in self.items:
            if item.identifier == new_item.identifier:
                return True
        return False


class ShoppingListRepository(ABC):
    @abstractmethod
    def add_item(self, item: Item, user_id: int) -> ShoppingList:
        pass

    @abstractmethod
    def get_current_list(self, user_id: int) -> ShoppingList:
        pass
