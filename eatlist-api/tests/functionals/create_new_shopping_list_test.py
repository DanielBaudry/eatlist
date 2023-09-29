from sqlmodel import select

from infra.database.models.shopping_list import ShoppingListSQL


class CreateNewShoppingListTest:
    def should_create_new_empty_shopping_list(self, session, client):
        # given / when
        response = client.post(
            "/shoplists/"
        )

        # then
        assert response.status_code == 201
        data = response.json()
        assert data == {"response": "ok"}
        result = session.exec(select(ShoppingListSQL)).all()
        assert len(result) == 1
