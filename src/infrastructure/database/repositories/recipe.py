from itertools import groupby
from typing import List

from src.domain.recipe import RecipeRepository, Recipe
from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db
from src.infrastructure.database.models.recipe_item_sql_entity import RecipeItemSQLEntity
from src.infrastructure.database.models.recipe_sql_entity import RecipeSQLEntity
from src.infrastructure.database.repositories import item


def to_domain(available_recipes: List[object]) -> List[Recipe]:
    recipes = []
    for recipe_name, group in groupby(available_recipes, lambda r: r.name):
        recipes.append(
            Recipe(
                name=recipe_name,
                items=[item.to_domain(it[1]) for it in group]
            )
        )
    return recipes


class RecipeRepositorySQL(RecipeRepository):
    def get_recipes(self) -> List[Recipe]:
        available_recipes_with_items = db.session.query(RecipeItemSQLEntity) \
            .join(RecipeSQLEntity, RecipeSQLEntity.id == RecipeItemSQLEntity.recipeId) \
            .outerjoin(ItemSQLEntity, RecipeItemSQLEntity.itemId == ItemSQLEntity.id) \
            .with_entities(RecipeSQLEntity.name, ItemSQLEntity) \
            .all()

        return to_domain(available_recipes_with_items)
