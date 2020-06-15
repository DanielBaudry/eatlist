from datetime import datetime
from typing import List, Optional

from src.domain.item import Item, ALL_YEAR
from src.domain.recommended_item import RecommendedItem
from src.domain.shopping_list import ShoppingListRepository, ShoppingList
from src.domain.shopping_list_history import ShoppingListHistory
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


def to_shopping_list_history(history: object) -> ShoppingListHistory:
    return ShoppingListHistory([user_item_date.shopping_date for user_item_date in history])


def to_recommendation_list(existing_user_items: List[object]) -> List[RecommendedItem]:
    print(existing_user_items[0])
    return [RecommendedItem(
        identifier=existing_user_item.id,
        name=existing_user_item.name,
        season_calendar=existing_user_item.seasonal_calendar if existing_user_item.seasonal_calendar else ALL_YEAR,
        shopping_item_id=existing_user_item.shopping_item_id,
        shopping_date=existing_user_item.shopping_date,
    ) for existing_user_item in existing_user_items]


class ShoppingListRepositorySQL(ShoppingListRepository):
    def get_all_shopping_list(self, user_id: int) -> List[ShoppingList]:
        existing_user_items = db.session.query(UserItemSQLEntity) \
            .join(ItemSQLEntity, ItemSQLEntity.id == UserItemSQLEntity.itemId) \
            .filter(UserItemSQLEntity.shopping_date != None) \
            .with_entities(UserItemSQLEntity.id.label('shopping_item_id'),
                           UserItemSQLEntity.shopping_date,
                           UserItemSQLEntity.itemId.label('id'),
                           ItemSQLEntity.name,
                           ItemSQLEntity.seasonal_calendar) \
            .all()
        return to_recommendation_list(existing_user_items)

    def get_history(self, user_id: int) -> ShoppingListHistory:
        user_item_dates = db.session.query(UserItemSQLEntity) \
            .filter(UserItemSQLEntity.shopping_date != None) \
            .group_by(UserItemSQLEntity.shopping_date) \
            .with_entities(UserItemSQLEntity.shopping_date) \
            .all()
        return to_shopping_list_history(user_item_dates)

    def update(self, shopping_list: ShoppingList) -> None:
        for item in shopping_list.items:
            existing_item = db.session.query(UserItemSQLEntity) \
                .filter(UserItemSQLEntity.itemId == item.identifier) \
                .filter(UserItemSQLEntity.userId == shopping_list.user_id) \
                .filter(UserItemSQLEntity.shopping_date == None) \
                .first()
            if not existing_item:
                self.add_item(item=item, user_id=shopping_list.user_id)

    def archive_current_list(self, user_id: int) -> None:
        db.session.query(UserItemSQLEntity) \
            .filter(UserItemSQLEntity.userId == user_id) \
            .filter(UserItemSQLEntity.shopping_date == None) \
            .update(dict(shopping_date=datetime.now()))
        db.session.commit()

    def remove_item(self, user_id: int, shopping_item_id: int) -> ShoppingList:
        user_item_sql_entity = db.session.query(UserItemSQLEntity) \
            .get(shopping_item_id)
        db.session.delete(user_item_sql_entity)
        db.session.commit()
        return self.get_shopping_list(user_id)

    def get_shopping_list(self, user_id: int, shopping_list_date: Optional[datetime] = None) -> ShoppingList:
        user_item_sql_entities = db.session.query(UserItemSQLEntity) \
            .join(ItemSQLEntity, ItemSQLEntity.id == UserItemSQLEntity.itemId) \
            .filter(UserItemSQLEntity.userId == user_id) \
            .filter(UserItemSQLEntity.shopping_date == shopping_list_date) \
            .with_entities(UserItemSQLEntity.id.label('shopping_item_id'),
                           ItemSQLEntity.id,
                           ItemSQLEntity.name,
                           ItemSQLEntity.seasonal_calendar) \
            .all()
        return to_domain(
            user_items=user_item_sql_entities,
            user_id=user_id
        )

    def add_item(self, item: Item, user_id: int) -> ShoppingList:
        new_user_item = UserItemSQLEntity()
        new_user_item.userId = user_id
        new_user_item.itemId = item.identifier
        db.session.add(new_user_item)
        db.session.commit()

        return self.get_shopping_list(user_id)
