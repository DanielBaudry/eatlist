from datetime import datetime
from typing import List

from src.domain.item import Item
from src.domain.shopping_list import ShoppingListRepository, ShoppingList
from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db
from src.infrastructure.database.models.user_item_sql_entity import UserItemSQLEntity
from src.infrastructure.database.repositories import user_item


def to_domain(user_items: List[object], user_id: int) -> ShoppingList:
    return ShoppingList(
        user_id=user_id,
        items=[
            user_item.to_domain(item) for item in user_items
        ]
    )


class ShoppingListRepositorySQL(ShoppingListRepository):
    def archive_current_list(self, user_id: int) -> None:
        db.session.query(UserItemSQLEntity) \
            .filter(UserItemSQLEntity.userId == user_id) \
            .update(dict(shopping_date=datetime.now()))
        db.session.commit()

    def remove_item(self, user_id: int, shopping_item_id: int) -> ShoppingList:
        user_item_sql_entity = db.session.query(UserItemSQLEntity)\
            .get(shopping_item_id)
        db.session.delete(user_item_sql_entity)
        db.session.commit()
        return self.get_current_list(user_id)

    def get_current_list(self, user_id: int) -> ShoppingList:
        return to_domain(
            user_items=db.session.query(UserItemSQLEntity) \
                .join(ItemSQLEntity, ItemSQLEntity.id == UserItemSQLEntity.itemId) \
                .filter(UserItemSQLEntity.userId == user_id) \
                .filter(UserItemSQLEntity.shopping_date == None) \
                .with_entities(UserItemSQLEntity.id.label('shopping_item_id'),
                               ItemSQLEntity.id,
                               ItemSQLEntity.name) \
                .all(),
            user_id=user_id
        )

    def add_item(self, item: Item, user_id: int) -> ShoppingList:
        new_user_item = UserItemSQLEntity()
        new_user_item.userId = user_id
        new_user_item.itemId = item.identifier
        db.session.add(new_user_item)
        db.session.commit()

        return self.get_current_list(user_id)
