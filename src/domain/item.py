from abc import ABC, abstractmethod


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
    def add_item_to_referential(self, new_item_name: str) -> Item:
        pass
