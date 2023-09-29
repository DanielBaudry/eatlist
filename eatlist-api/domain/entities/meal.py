from typing import List

from sqlmodel import SQLModel

from domain.entities.item import ItemBase


class MealBase(SQLModel):
    name: str


class MealWithItems(MealBase):
    items: List[ItemBase] = []


class MealForShoppingList(MealBase):
    id: int
