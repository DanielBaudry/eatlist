from itertools import groupby
from typing import List

from src.domain.recipe import RecipeRepository, Recipe
from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db
from src.infrastructure.database.models.recipe_item_sql_entity import RecipeItemSQLEntity
from src.infrastructure.database.models.recipe_sql_entity import RecipeSQLEntity
from src.infrastructure.database.repositories import item


def list_to_domain(available_recipes: List[object]) -> List[Recipe]:
    recipes = []
    for recipe_name, group in groupby(available_recipes, lambda r: r.name):
        recipe_items = []
        recipe_id = None
        for it in group:
            recipe_id = it.id
            recipe_items.append(item.to_domain(it[2]))
        recipes.append(
            Recipe(
                identifier=recipe_id,
                name=recipe_name,
                items=recipe_items
            )
        )
    return recipes


def to_domain(recipe_sql_entity: RecipeSQLEntity) -> Recipe:
    return Recipe(
        identifier=recipe_sql_entity.id,
        name=recipe_sql_entity.name,
        items=[item.to_domain(it) for it in recipe_sql_entity.items]
    )


class RecipeRepositorySQL(RecipeRepository):
    def get_recipe(self, recipe_id: int) -> Recipe:
        recipe_sql_entity = db.session.query(RecipeSQLEntity).get(recipe_id)
        return to_domain(recipe_sql_entity)

    def get_recipes(self) -> List[Recipe]:
        available_recipes_with_items = db.session.query(RecipeItemSQLEntity) \
            .join(RecipeSQLEntity, RecipeSQLEntity.id == RecipeItemSQLEntity.recipeId) \
            .outerjoin(ItemSQLEntity, RecipeItemSQLEntity.itemId == ItemSQLEntity.id) \
            .with_entities(RecipeSQLEntity.id, RecipeSQLEntity.name, ItemSQLEntity) \
            .all()

        return list_to_domain(available_recipes_with_items)
