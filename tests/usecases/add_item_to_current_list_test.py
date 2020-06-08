from unittest.mock import MagicMock

from src.domain.item import Item
from src.infrastructure.database.repositories.item import ItemRepositorySQL
from src.infrastructure.database.repositories.shopping_list import ShoppingListRepositorySQL
from src.usecases.add_item_to_current_list import AddItemToCurrentList


class AddItemToCurrentListTest:
    def setup_method(self):
        self.item_repository = ItemRepositorySQL()
        self.item_repository.convert_item_from_name = MagicMock()
        self.shopping_list_repository = ShoppingListRepositorySQL()
        self.shopping_list_repository.add_item = MagicMock()
        self.add_item_to_current_list = AddItemToCurrentList(
            self.item_repository,
            self.shopping_list_repository
        )

    def should_add_item_to_current_user_shopping_list(self):
        # Given
        item_name = 'Cacao'
        user_id = 5
        item = Item(identifier=12, name='Caco')
        self.item_repository.convert_item_from_name.return_value = item

        # When
        self.add_item_to_current_list.execute(new_item_name=item_name,
                                              user_id=user_id)

        # Then
        self.item_repository.convert_item_from_name.assert_called_once_with(item_name)
        self.shopping_list_repository.add_item.assert_called_once_with(item, user_id)
