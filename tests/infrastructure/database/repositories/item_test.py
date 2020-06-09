from pytest import fixture

from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db
from src.infrastructure.database.repositories.item import ItemRepositorySQL
from tests.conftest import clean_database


class ItemRepositorySQLTest:
    class ConvertItemFromNameTest:
        def setup_method(self):
            self.item_repository_sql = ItemRepositorySQL()

        @clean_database
        def should_return_item_when_name_matches(self, app: fixture):
            # Given
            item = ItemSQLEntity()
            item.name = 'Chocolat'
            db.session.add(item)
            db.session.commit()

            item_name = 'Chocolat'

            # When
            item_result = self.item_repository_sql.add_item_to_referential(item_name)

            # Then
            assert db.session.query(ItemSQLEntity).count() == 1
            assert item_result.identifier == item.id

        @clean_database
        def should_add_new_item_when_name_does_not_exist(self, app: fixture):
            # Given
            item = ItemSQLEntity()
            item.name = 'Lait'
            db.session.add(item)
            db.session.commit()

            item_name = 'Chocolat'

            # When
            item_result = self.item_repository_sql.add_item_to_referential(item_name)

            # Then
            assert db.session.query(ItemSQLEntity).count() == 2
            assert item_result.name == item_name

        @clean_database
        def should_get_existing_item_when_case_does_not_match(self, app: fixture):
            # Given
            item = ItemSQLEntity()
            item.name = 'chocolat'
            db.session.add(item)
            db.session.commit()

            item_name = 'Chocolat'

            # When
            item_result = self.item_repository_sql.add_item_to_referential(item_name)

            # Then
            assert db.session.query(ItemSQLEntity).count() == 1
            assert item_result.identifier == item.id
