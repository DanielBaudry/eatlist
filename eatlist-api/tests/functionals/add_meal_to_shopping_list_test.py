from datetime import datetime

from sqlmodel import select

from infra.database.models.item import Item
from infra.database.models.meal_sql import MealSQL
from infra.database.models.shopping_list import ShoppingListSQL


class AddMealToShoppingListTest:
    def should_add_meal_to_shopping_list(self, session, client):
        # given
        items = [
            Item(id=123, name="Pâtes"),
            Item(id=456, name="Pesto"),
            Item(id=789, name="Parmesan"),
        ]
        meal = MealSQL(id=123, name="Pâtes pesto", items=items)
        shopping_list = ShoppingListSQL(id=123, date=datetime(year=2023, month=9, day=29))
        session.add(meal)
        session.add(shopping_list)
        session.commit()

        # when
        response = client.patch(
            "/shoplists/123",
            json={
                "name": "Pâtes pesto",
                "id": 123,
            }
        )

        # then
        assert response.status_code == 200
        data = response.json()
        assert data == {"response": "ok"}
        result = session.exec(select(ShoppingListSQL)).all()
        assert len(result) == 1
        assert result[0].items == [
            Item(id=123, meal_id=123, name="Pâtes"),
            Item(id=456, meal_id=123, name="Pesto"),
            Item(id=789, meal_id=123, name="Parmesan"),
        ]
