from datetime import datetime

import bcrypt
from freezegun import freeze_time
from pytest import fixture

from src.infrastructure.database.models import ItemSQLEntity, UserSQLEntity, UserItemSQLEntity
from src.infrastructure.database.models.db import db
from src.infrastructure.database.repositories.shopping_list import ShoppingListRepositorySQL
from tests.conftest import clean_database


class ShoppingListRepositorySQLTest:
    class RemoveItemTest:
        def setup_method(self):
            self.shopping_list_repository_sql = ShoppingListRepositorySQL()

        @clean_database
        def should_remove_item_from_user_items(self, app: fixture):
            # Given
            item = ItemSQLEntity()
            item.name = 'Chocolat'
            db.session.add(item)

            user = UserSQLEntity()
            user.username = 'Toto'
            user.password = bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt())
            db.session.add(user)
            db.session.commit()

            user_item = UserItemSQLEntity()
            user_item.userId = user.id
            user_item.itemId = item.id
            db.session.add(user_item)
            db.session.commit()

            # When
            shopping_list_result = self.shopping_list_repository_sql.remove_item(
                user_id=user.id,
                shopping_item_id=user_item.id
            )

            # Then
            assert db.session.query(ItemSQLEntity).count() == 1
            assert db.session.query(UserItemSQLEntity).count() == 0
            assert len(shopping_list_result.items) == 0

    class GetCurrentListTest:
        def setup_method(self):
            self.shopping_list_repository_sql = ShoppingListRepositorySQL()

        @clean_database
        def should_return_all_items_for_specified_user(self, app: fixture) -> None:
            # Given
            item = ItemSQLEntity()
            item.name = 'Chocolat'
            db.session.add(item)

            user = UserSQLEntity()
            user.username = 'Toto'
            user.password = bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt())
            db.session.add(user)
            db.session.commit()

            user_item = UserItemSQLEntity()
            user_item.userId = user.id
            user_item.itemId = item.id
            db.session.add(user_item)
            db.session.commit()

            # When
            shopping_list_result = self.shopping_list_repository_sql.get_shopping_list(user.id, None)

            # Then
            assert len(shopping_list_result.items) == 1
            assert shopping_list_result.items[0].identifier == item.id

        @clean_database
        def should_not_return_items_with_shopping_date(self, app: fixture) -> None:
            # Given
            item = ItemSQLEntity()
            item.name = 'Chocolat'
            db.session.add(item)

            user = UserSQLEntity()
            user.username = 'Toto'
            user.password = bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt())
            db.session.add(user)
            db.session.commit()

            user_item = UserItemSQLEntity()
            user_item.userId = user.id
            user_item.itemId = item.id
            user_item.shopping_date = datetime.now()
            db.session.add(user_item)
            db.session.commit()

            # When
            shopping_list_result = self.shopping_list_repository_sql.get_shopping_list(user.id, None)

            # Then
            assert len(shopping_list_result.items) == 0

    class ArchiveCurrentListTest:
        def setup_method(self):
            self.shopping_list_repository_sql = ShoppingListRepositorySQL()

        @freeze_time('2020-01-01 12:00:00')
        @clean_database
        def should_set_current_date_to_all_items_for_specified_user(self, app: fixture) -> None:
            # Given
            item = ItemSQLEntity()
            item.name = 'Chocolat'
            db.session.add(item)

            user = UserSQLEntity()
            user.username = 'Toto'
            user.password = bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt())
            db.session.add(user)
            db.session.commit()

            user_item = UserItemSQLEntity()
            user_item.userId = user.id
            user_item.itemId = item.id
            db.session.add(user_item)
            db.session.commit()

            # When
            self.shopping_list_repository_sql.archive_current_list(user_id=user.id)

            # Then
            user_item_updated = db.session.query(UserItemSQLEntity).first()
            assert user_item_updated.shopping_date == datetime(2020, 1, 1, 12)

        @clean_database
        def should_not_modify_date_for_already_shopped_items_for_specified_user(self, app: fixture) -> None:
            # Given
            item = ItemSQLEntity()
            item.name = 'Chocolat'
            db.session.add(item)

            user = UserSQLEntity()
            user.username = 'Toto'
            user.password = bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt())
            db.session.add(user)
            db.session.commit()

            user_item = UserItemSQLEntity()
            user_item.userId = user.id
            user_item.itemId = item.id
            user_item.shopping_date = datetime(2018, 1, 23)
            db.session.add(user_item)
            db.session.commit()

            # When
            self.shopping_list_repository_sql.archive_current_list(user_id=user.id)

            # Then
            user_item_updated = db.session.query(UserItemSQLEntity).first()
            assert user_item_updated.shopping_date == datetime(2018, 1, 23)

    class GetHistoryTest:
        def setup_method(self):
            self.shopping_list_repository_sql = ShoppingListRepositorySQL()

        @clean_database
        def should_get_all_dates_for_archived_shopping_list(self, app: fixture) -> None:
            # Given
            item = ItemSQLEntity()
            item.name = 'Chocolat'
            db.session.add(item)

            user = UserSQLEntity()
            user.username = 'Toto'
            user.password = bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt())
            db.session.add(user)
            db.session.commit()

            user_item1 = UserItemSQLEntity()
            user_item1.userId = user.id
            user_item1.itemId = item.id
            user_item1.shopping_date = datetime(2019, 1, 5)
            db.session.add(user_item1)

            user_item2 = UserItemSQLEntity()
            user_item2.userId = user.id
            user_item2.itemId = item.id
            user_item2.shopping_date = None
            db.session.add(user_item2)
            db.session.commit()

            # When
            history_result = self.shopping_list_repository_sql.get_history(user_id=user.id)

            # Then
            assert history_result.shopping_list_date == [datetime(2019, 1, 5)]
