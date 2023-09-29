from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from infra.database.models.meal import Meal


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str

    meal_id: Optional[int] = Field(default=None, foreign_key="meal.id")

    meal: Optional[Meal] = Relationship(back_populates="items")
