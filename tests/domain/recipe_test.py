from src.domain.item import Item
from src.domain.recipe import Recipe


class RecipeTest:
    class AvailableWithItemsTest:
        def should_return_false_when_not_all_items_are_present(self):
            # Given
            item1 = Item(
                identifier=12,
                name='Riz'
            )
            item2 = Item(
                identifier=2,
                name='Tomates'
            )
            recipe = Recipe(
                identifier=13,
                name='Riz tomate',
                items=[
                    item1,
                    item2
                ]
            )

            # When
            result = recipe.available_with_items([
                Item(
                    identifier=12,
                    name='Riz'
                )
            ])

            # Then
            assert not result

        def should_return_true_when_all_items_are_present(self):
            # Given
            item1 = Item(
                identifier=12,
                name='Riz'
            )
            item2 = Item(
                identifier=2,
                name='Tomates'
            )
            recipe = Recipe(
                identifier=4,
                name='Riz tomate',
                items=[
                    item1,
                    item2
                ]
            )

            # When
            result = recipe.available_with_items([
                Item(
                    identifier=12,
                    name='Riz'
                ),
                Item(
                    identifier=2,
                    name='Tomates'
                ),
                Item(
                    identifier=5,
                    name='Pâtes'
                )
            ])

            # Then
            assert result
