from src.domain.item import ALL_YEAR
from src.domain.shopping_list_item import ShoppingListItem
from src.infrastructure.database.models.user_item_sql_entity import UserItemSQLEntity


def to_domain(user_item: UserItemSQLEntity) -> ShoppingListItem:
    seasonal_calendar = user_item.seasonal_calendar if user_item.seasonal_calendar else ALL_YEAR
    return ShoppingListItem(
        shopping_item_id=user_item.shopping_item_id,
        identifier=user_item.id,
        name=user_item.name,
        season_calendar=seasonal_calendar,
    )
