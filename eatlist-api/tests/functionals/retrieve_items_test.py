from infra.database.models.item import Item


class RetrieveItemsTest:
    def should_retrieve_all_registered_items(self, session, client):
        # given
        items = [
            Item(id=123, name="Pâtes"),
            Item(id=456, name="Pesto"),
            Item(id=789, name="Parmesan"),
        ]
        session.add_all(items)
        session.commit()

        # when
        response = client.get(
            "/items/"
        )

        # then
        assert response.status_code == 200
        data = response.json()
        assert data == [
            {'name': 'Pâtes'},
            {'name': 'Pesto'},
            {'name': 'Parmesan'}
        ]
