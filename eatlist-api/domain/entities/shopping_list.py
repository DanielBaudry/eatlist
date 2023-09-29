from datetime import datetime
from typing import List

from sqlmodel import SQLModel

from domain.entities.format.date import convert_datetime_to_iso_8601_with_timezone
from domain.entities.item import ItemBase


class ShoppingListBase(SQLModel):
    date: datetime

    class Config:
        json_encoders = {
            datetime: convert_datetime_to_iso_8601_with_timezone
        }


class ShoppingListWithItems(ShoppingListBase):
    items: List[ItemBase] = []
