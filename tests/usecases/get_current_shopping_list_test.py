from unittest.mock import MagicMock

from src.domain.item import Item
from src.infrastructure.database.repositories.shopping_list import ShoppingListRepositorySQL
from src.usecases.get_current_shopping_list import GetCurrentShoppingList


class GetCurrentShoppingListTest:
    def setup_method(self):
        self.shopping_list_repository = ShoppingListRepositorySQL()
        self.shopping_list_repository.get_shopping_list = MagicMock()
        self.get_current_shopping_list = GetCurrentShoppingList(
            self.shopping_list_repository
        )

    def should_get_user_shopping_list(self):
        # Given
        user_id = 7
        shopping_list = [
            Item(identifier=12, name='Caco'),
            Item(identifier=26, name='Lait')
        ]
        self.shopping_list_repository.get_shopping_list.return_value = shopping_list

        # When
        self.get_current_shopping_list.execute(user_id=user_id)

        # Then
        self.shopping_list_repository.get_shopping_list.assert_called_once_with(user_id, None)
