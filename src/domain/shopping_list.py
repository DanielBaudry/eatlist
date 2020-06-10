from abc import abstractmethod, ABC
from datetime import datetime
from typing import List, Optional

from src.domain.item import Item
from src.domain.shopping_list_history import ShoppingListHistory
from src.domain.shopping_list_item import ShoppingListItem


class ShoppingList:
    def __init__(self, user_id: int, items: List[ShoppingListItem] = []):
        self.user_id = user_id
        self.items = items

    def already_contains(self, new_item: Item) -> bool:
        for item in self.items:
            if item.identifier == new_item.identifier:
                return True
        return False

    def add_item(self, new_item: Item) -> None:
        if not self.already_contains(new_item):
            self.items.append(
                ShoppingListItem(
                    identifier=new_item.identifier,
                    name=new_item.name,
                    shopping_item_id=0
                )
            )

    def add_items(self, items: List[Item]) -> None:
        for item in items:
            self.add_item(item)


class ShoppingListRepository(ABC):
    @abstractmethod
    def add_item(self, item: Item, user_id: int) -> ShoppingList:
        pass

    @abstractmethod
    def get_shopping_list(self, user_id: int, shopping_list_date: Optional[datetime] = None) -> ShoppingList:
        pass

    @abstractmethod
    def remove_item(self, user_id: int, shopping_item_id: int) -> ShoppingList:
        pass

    @abstractmethod
    def archive_current_list(self, user_id: int) -> None:
        pass

    @abstractmethod
    def update(self, shopping_list: ShoppingList):
        pass

    @abstractmethod
    def get_history(self, user_id: int) -> ShoppingListHistory:
        pass
