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
            ['Chou', 1, 5],
            ['Banane', 3, 12]
        ])

        # When
        _save_new_item_to_database(csv_reader_mock)

        # Then
        assert db.session.query(ItemSQLEntity).count() == 2
        item_chou = db.session.query(ItemSQLEntity).filter(ItemSQLEntity.name == 'Chou').one()
        item_banana = db.session.query(ItemSQLEntity).filter(ItemSQLEntity.name == 'Banane').one()
        assert item_chou.seasonal_calendar == [
            True, True, True, True, True, False, False, False, False, False, False, False,
        ]
        assert item_banana.seasonal_calendar == [
            False, False, True, True, True, True, True, True, True, True, True, True,
        ]
