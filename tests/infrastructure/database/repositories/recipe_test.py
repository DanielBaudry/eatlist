from pytest import fixture

from src.domain.item import Item
from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db
from src.infrastructure.database.models.recipe_item_sql_entity import RecipeItemSQLEntity
from src.infrastructure.database.models.recipe_sql_entity import RecipeSQLEntity
from src.infrastructure.database.repositories.recipe import RecipeRepositorySQL
from tests.conftest import clean_database


class RecipeRepositorySQLTest:
    class GetRecipesTest:
        def setup_method(self):
            self.recipe_repository_sql = RecipeRepositorySQL()

        @clean_database
        def should_get_all_recipes_with_items(self, app: fixture):
            # Given
            item1 = ItemSQLEntity()
            item1.name = 'Chocolat'
            db.session.add(item1)

            item2 = ItemSQLEntity()
            item2.name = 'Lait'
            db.session.add(item2)

            recipe1 = RecipeSQLEntity()
            recipe1.name = 'Chocolat chaud'
            db.session.add(recipe1)

            recipe2 = RecipeSQLEntity()
            recipe2.name = 'Chocolat'
            db.session.add(recipe2)
            db.session.commit()

            recipe_item1 = RecipeItemSQLEntity()
            recipe_item1.recipeId = recipe1.id
            recipe_item1.itemId = item1.id
            db.session.add(recipe_item1)

            recipe_item2 = RecipeItemSQLEntity()
            recipe_item2.recipeId = recipe1.id
            recipe_item2.itemId = item2.id
            db.session.add(recipe_item2)

            recipe_item3 = RecipeItemSQLEntity()
            recipe_item3.recipeId = recipe2.id
            recipe_item3.itemId = item1.id
            db.session.add(recipe_item3)

            db.session.commit()

            # When
            available_recipes = self.recipe_repository_sql.get_recipes()

            # Then

            assert len(available_recipes) == 2
            assert available_recipes[0].name == 'Chocolat chaud'
            assert len(available_recipes[0].items) == 2
            assert all(isinstance(r, Item) for r in available_recipes[0].items)
            assert available_recipes[1].name == 'Chocolat'
            assert len(available_recipes[1].items) == 1

    class GetRecipeTest:
        def setup_method(self):
            self.recipe_repository_sql = RecipeRepositorySQL()

        @clean_database
        def should_get_matching_recipe(self, app: fixture):
            # Given
            item1 = ItemSQLEntity()
            item1.name = 'Chocolat'
            db.session.add(item1)

            item2 = ItemSQLEntity()
            item2.name = 'Lait'
            db.session.add(item2)

            recipe1 = RecipeSQLEntity()
            recipe1.name = 'Chocolat chaud'
            db.session.add(recipe1)
            db.session.commit()

            recipe_item1 = RecipeItemSQLEntity()
            recipe_item1.recipeId = recipe1.id
            recipe_item1.itemId = item1.id
            db.session.add(recipe_item1)

            recipe_item2 = RecipeItemSQLEntity()
            recipe_item2.recipeId = recipe1.id
            recipe_item2.itemId = item2.id
            db.session.add(recipe_item2)
            db.session.commit()

            # When
            recipe_result = self.recipe_repository_sql.get_recipe(recipe1.id)

            # Then

            assert recipe_result.name == 'Chocolat chaud'
            assert len(recipe_result.items) == 2
