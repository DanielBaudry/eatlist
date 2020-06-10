from abc import ABC, abstractmethod
from typing import List


class Item:
    def __init__(self, identifier: int, name: str):
        self.identifier = identifier
        self.name = name

    def __eq__(self, other) -> bool:
        return self.identifier == other.identifier

    def __hash__(self):
        return self.identifier


class ItemRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Item]:
        pass

    @abstractmethod
    def add_item_to_referential(self, new_item_name: str) -> Item:
        pass
