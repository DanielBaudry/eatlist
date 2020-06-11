from pytest import fixture

from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db
from src.infrastructure.database.referential.import_items import _save_new_item_to_database
from tests.conftest import clean_database


class SaveNewItemToDatabaseTest:
    @clean_database
    def should_save_items_in_database_if_not_exists(self, app: fixture) -> None:
        # Given
        csv_reader_mock = iter([
            ['Chou'],
            ['Banane']
        ])

        # When
        _save_new_item_to_database(csv_reader_mock)

        # Then
        assert db.session.query(ItemSQLEntity).count() == 2
        assert db.session.query(ItemSQLEntity).filter(ItemSQLEntity.name == 'Chou').count() == 1
        assert db.session.query(ItemSQLEntity).filter(ItemSQLEntity.name == 'Banane').count() == 1
