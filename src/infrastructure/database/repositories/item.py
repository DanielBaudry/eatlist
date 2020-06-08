from src.domain.item import ItemRepository, Item
from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db


def to_domain(item_sql_entity: ItemSQLEntity) -> Item:
    return Item(
        identifier=item_sql_entity.id,
        name=item_sql_entity.name
    )


class ItemRepositorySQL(ItemRepository):
    def convert_item_from_name(self, new_item_name: str) -> Item:
        existing_item = db.session.query(ItemSQLEntity) \
            .filter(ItemSQLEntity.name == new_item_name) \
            .first()
        if not existing_item:
            existing_item = ItemSQLEntity()
            existing_item.name = new_item_name
            db.session.add(existing_item)
            db.session.commit()
        return to_domain(existing_item)
