from typing import List

from sqlalchemy import func

from src.domain.item import ItemRepository, Item, ALL_YEAR
from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db


def to_domain(item_sql_entity: ItemSQLEntity) -> Item:
    seasonal_calendar = item_sql_entity.seasonal_calendar if item_sql_entity.seasonal_calendar else ALL_YEAR
    return Item(
        identifier=item_sql_entity.id,
        name=item_sql_entity.name,
        season_calendar=seasonal_calendar,
    )


class ItemRepositorySQL(ItemRepository):
    def get_all(self) -> List[Item]:
        items = db.session.query(ItemSQLEntity).all()
        return [to_domain(item) for item in items]

    def add_item_to_referential(self, new_item_name: str) -> Item:
        existing_item = db.session.query(ItemSQLEntity) \
            .filter(func.lower(ItemSQLEntity.name) == func.lower(new_item_name)) \
            .first()
        if not existing_item:
            existing_item = ItemSQLEntity()
            existing_item.name = new_item_name
            db.session.add(existing_item)
            db.session.commit()
        return to_domain(existing_item)
