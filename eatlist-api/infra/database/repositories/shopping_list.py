from datetime import datetime

from domain.entities.meal import MealBase, MealForShoppingList
from domain.entities.shopping_list import ShoppingListBase, UpdateShoppingList
from domain.repositories.shopping_list import ShoppingListRepo

from sqlmodel import Session, select

from infra.database.models.meal_sql import MealSQL
from infra.database.models.shopping_list import ShoppingListSQL


class ShoppingListRepoSQL(ShoppingListRepo):

    def __init__(self, session: Session):
        self.session = session

    def create(self) -> ShoppingListBase:
        shoplist = ShoppingListSQL(date=datetime.utcnow())
        self.session.add(shoplist)
        self.session.commit()
        return shoplist

    def add_meal(self, shopping_list_id: int, meal: MealForShoppingList):
        existing_shopping_list = self.session.exec(
            select(ShoppingListSQL).where(ShoppingListSQL.id == shopping_list_id)
        ).one()
        existing_meal = self.session.exec(select(MealSQL).where(MealSQL.id == meal.id)).one()
        existing_shopping_list.items = existing_meal.items
        self.session.add(existing_shopping_list)
        self.session.commit()
