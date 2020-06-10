from unittest.mock import MagicMock

from src.domain.item import Item
from src.domain.shopping_list import ShoppingList
from src.domain.shopping_list_item import ShoppingListItem
from src.infrastructure.database.repositories.item import ItemRepositorySQL
from src.infrastructure.database.repositories.shopping_list import ShoppingListRepositorySQL
from src.usecases.add_item_to_current_list import AddItemToCurrentList


class AddItemToCurrentListTest:
    def setup_method(self):
        self.item_repository = ItemRepositorySQL()
        self.item_repository.add_item_to_referential = MagicMock()
        self.shopping_list_repository = ShoppingListRepositorySQL()
        self.shopping_list_repository.get_current_list = MagicMock()
        self.shopping_list_repository.update = MagicMock()
        self.add_item_to_current_list = AddItemToCurrentList(
            self.item_repository,
            self.shopping_list_repository
        )

    def should_add_item_to_current_user_shopping_list(self):
        # Given
        item_name = 'Cacao'
        user_id = 5
        item = Item(identifier=12, name='Caco')
        self.item_repository.add_item_to_referential.return_value = item
        shopping_list = ShoppingList(
            user_id=user_id,
            items=[
                ShoppingListItem(
                    shopping_item_id=1,
                    identifier=26,
                    name='Lait'
                )
            ]
        )
        self.shopping_list_repository.get_current_list.return_value = shopping_list

        # When
        self.add_item_to_current_list.execute(new_item_name=item_name,
                                              user_id=user_id)

        # Then
        self.item_repository.add_item_to_referential.assert_called_once_with(item_name)
        self.shopping_list_repository.get_current_list.assert_called_once_with(user_id)
        self.shopping_list_repository.update.assert_called_once_with(shopping_list)
