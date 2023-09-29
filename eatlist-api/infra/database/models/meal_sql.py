from typing import Optional, List

from sqlmodel import Field, Relationship

from domain.entities.meal import MealBase


class MealSQL(MealBase, table=True):
    __tablename__: str = "meal"

    id: Optional[int] = Field(default=None, primary_key=True)

    items: List["Item"] = Relationship(back_populates="meal")
