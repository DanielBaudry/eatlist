from unittest.mock import MagicMock

from src.domain.item import Item
from src.domain.shopping_list import ShoppingList
from src.infrastructure.database.repositories.item import ItemRepositorySQL
from src.infrastructure.database.repositories.shopping_list import ShoppingListRepositorySQL
from src.usecases.add_item_to_current_list import AddItemToCurrentList
from src.usecases.remove_item_from_current_shopping_list import RemoveItemFromCurrentShoppingList


class RemoveItemFromCurrentShoppingListTest:
    def setup_method(self):
        self.shopping_list_repository = ShoppingListRepositorySQL()
        self.shopping_list_repository.remove_item = MagicMock()
        self.remove_item_from_current_list = RemoveItemFromCurrentShoppingList(
            self.shopping_list_repository
        )

    def should_remove_item_from_current_user_shopping_list(self):
        # Given
        user_item_id = 6
        user_id = 5

        # When
        self.remove_item_from_current_list.execute(user_item_id=user_item_id, user_id=user_id)

        # Then
        self.shopping_list_repository.remove_item.assert_called_once_with(user_id, user_item_id)

