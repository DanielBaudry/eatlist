from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class MealBase(SQLModel):
    name: str


class Meal(MealBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    items: List["Item"] = Relationship(back_populates="meal")
