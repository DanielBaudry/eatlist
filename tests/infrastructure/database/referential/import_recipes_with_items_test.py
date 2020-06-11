from pytest import fixture

from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db
from src.infrastructure.database.models.recipe_item_sql_entity import RecipeItemSQLEntity
from src.infrastructure.database.models.recipe_sql_entity import RecipeSQLEntity
from src.infrastructure.database.referential.import_recipes_with_items import _save_new_recipes_with_items
from tests.conftest import clean_database


class SaveNewRecipesWithItemsTest:
    @clean_database
    def should_save_recipes_with_items_in_database_if_not_exists(self, app: fixture) -> None:
        # Given
        csv_reader_mock = iter([
            ['Riz Lentilles', 'Riz', 'Lentilles', 'Carottes'],
            ['Banana Bread Cake', 'Banane', 'Chocolat', 'Farine', 'Oeufs', 'Levure']
        ])

        # When
        _save_new_recipes_with_items(csv_reader_mock)

        # Then
        assert db.session.query(ItemSQLEntity).count() == 8
        assert db.session.query(RecipeSQLEntity).count() == 2
        assert db.session.query(RecipeItemSQLEntity).count() == 8
