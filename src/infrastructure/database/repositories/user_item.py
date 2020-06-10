from src.domain.shopping_list import ShoppingList
from src.domain.shopping_list_item import ShoppingListItem
from src.infrastructure.database.models.user_item_sql_entity import UserItemSQLEntity


def to_domain(user_item: UserItemSQLEntity) -> ShoppingListItem:
    return ShoppingListItem(
        shopping_item_id=user_item.shopping_item_id,
        identifier=user_item.id,
        name=user_item.name,
    )

