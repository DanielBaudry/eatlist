from abc import ABC, abstractmethod


class Item:
    def __init__(self, identifier: int, name: str):
        self.identifier = identifier
        self.name = name


class ItemRepository(ABC):
    @abstractmethod
    def add_item_to_referential(self, new_item_name: str) -> Item:
        pass
