from src.domain.item import Item
from src.domain.shopping_list import ShoppingList


class ShoppingListTest:
    class AlreadyContainsTest:
        def should_return_false_when_item_is_not_in_list(self):
            # Given
            item = Item(
                identifier=12,
                name='Riz'
            )
            shopping_list = ShoppingList(
                user_id=5,
                items=[]
            )

            # When
            result = shopping_list.already_contains(item)

            # Then
            assert not result

        def should_return_true_when_item_is_already_in_list(self):
            # Given
            item = Item(
                identifier=12,
                name='Riz'
            )
            shopping_list = ShoppingList(
                user_id=5,
                items=[
                    Item(
                        identifier=12,
                        name='Riz'
                    )
                ]
            )

            # When
            result = shopping_list.already_contains(item)

            # Then
            assert result
