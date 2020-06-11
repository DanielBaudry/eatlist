from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

ALL_YEAR = [True for month in range(12)]


class Item:
    def __init__(self, identifier: int, name: str, season_calendar: List[bool] = ALL_YEAR):
        self.identifier = identifier
        self.name = name
        self.season_calendar = season_calendar

    def __eq__(self, other) -> bool:
        return self.identifier == other.identifier

    def __hash__(self):
        return self.identifier

    def is_seasonal(self) -> bool:
        return self.season_calendar[datetime.now().month - 1]


class ItemRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Item]:
        pass

    @abstractmethod
    def add_item_to_referential(self, new_item_name: str) -> Item:
        pass
