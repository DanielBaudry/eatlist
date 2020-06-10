from typing import List

from src.domain.item import ItemRepository, Item


class GetAllItems:
    def __init__(self, item_repostiory: ItemRepository):
        self.item_repostiory = item_repostiory

    def execute(self) -> List[Item]:
        return self.item_repostiory.get_all()
