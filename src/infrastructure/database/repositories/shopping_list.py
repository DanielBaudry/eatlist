from typing import List

from src.domain.item import Item
from src.domain.shopping_list import ShoppingListRepository, ShoppingList
from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db
from src.infrastructure.database.models.user_item_sql_entity import UserItemSQLEntity
from src.infrastructure.database.repositories import item


def to_domain(user_items: List[UserItemSQLEntity], user_id: int) -> ShoppingList:
    return ShoppingList(
        user_id=user_id,
        items=[item.to_domain(user_item) for user_item in user_items]
    )


class ShoppingListRepositorySQL(ShoppingListRepository):
    def get_current_list(self, user_id: int) -> ShoppingList:
        return to_domain(
            user_items=db.session.query(UserItemSQLEntity) \
                .join(ItemSQLEntity, ItemSQLEntity.id == UserItemSQLEntity.itemId) \
                .filter(UserItemSQLEntity.userId == user_id) \
                .with_entities(ItemSQLEntity.id,
                               ItemSQLEntity.name) \
                .all(),
            user_id=user_id
        )

    def add_item(self, item: Item, user_id: int) -> ShoppingList:
        user_item = UserItemSQLEntity()
        user_item.userId = user_id
        user_item.itemId = item.identifier
        db.session.add(user_item)
        db.session.commit()

        return self.get_current_list(user_id)
