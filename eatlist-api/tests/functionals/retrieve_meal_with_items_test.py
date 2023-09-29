from infra.database.models.item import Item
from infra.database.models.meal import Meal


class RetrieveMealsTest:
    def should_retrieve_all_registered_meal_with_items(self, session, client):
        # given
        items = [
            Item(id=123, name="Pâtes"),
            Item(id=456, name="Pesto"),
            Item(id=789, name="Parmesan"),
        ]
        meal = Meal(id=123, name="Pâtes pesto", items=items)
        session.add(meal)
        session.commit()

        # when
        response = client.get(
            "/meals/"
        )

        # then
        assert response.status_code == 200
        data = response.json()
        assert data == [
            {
                'name': 'Pâtes pesto',
                'items': [
                    {'id': 123, 'meal_id': 123, 'name': 'Pâtes'},
                    {'id': 456, 'meal_id': 123, 'name': 'Pesto'},
                    {'id': 789, 'meal_id': 123, 'name': 'Parmesan'}
                ]
            }
        ]
