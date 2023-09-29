from datetime import datetime

from infra.database.models.item import Item
from infra.database.models.shopping_list import ShoppingListSQL


class RetrieveShoppingListsTest:
    def should_retrieve_all_shopping_lists_with_items(self, session, client):
        # given
        items = [
            Item(id=123, name="Pâtes"),
            Item(id=456, name="Pesto"),
            Item(id=789, name="Parmesan"),
        ]
        shopping_list = ShoppingListSQL(id=123, date=datetime(year=2023, month=9, day=29), items=items)
        session.add(shopping_list)
        session.commit()

        # when
        response = client.get(
            "/shoplists/"
        )

        # then
        assert response.status_code == 200
        data = response.json()
        assert data == [
            {
                'date': '2023-09-29T00:00:00Z',
                'items': [
                    {'name': 'Pâtes'},
                    {'name': 'Pesto'},
                    {'name': 'Parmesan'}
                ]
            }
        ]
