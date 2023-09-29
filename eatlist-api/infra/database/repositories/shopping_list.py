from datetime import datetime

from domain.entities.shopping_list import ShoppingListBase
from domain.repositories.shopping_list import ShoppingListRepo

from sqlmodel import Session

from infra.database.models.shopping_list import ShoppingListSQL


class ShoppingListRepoSQL(ShoppingListRepo):
    def __init__(self, session: Session):
        self.session = session

    def create(self) -> ShoppingListBase:
        shoplist = ShoppingListSQL(date=datetime.utcnow())
        self.session.add(shoplist)
        self.session.commit()
        return shoplist
