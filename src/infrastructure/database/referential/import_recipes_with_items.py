import csv

from app import app
from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db
from src.infrastructure.database.models.recipe_item_sql_entity import RecipeItemSQLEntity
from src.infrastructure.database.models.recipe_sql_entity import RecipeSQLEntity


#
# CSV format: [nom de la recette],[nom de l'item1],[nom de l'item2],[...]
#
def import_recipes_with_items_in_database(csv_path: str) -> None:
    with app.app_context():
        csv_file = open(csv_path, newline='')
        csv_reader = csv.reader(csv_file, delimiter=',')
        _save_new_recipes_with_items(csv_reader)
        csv_file.close()
        print("Import terminé avec succès")


def _save_new_recipes_with_items(csv_reader: iter) -> None:
    for row in csv_reader:
        recipe_name = row[0]
        recipe = db.session.query(RecipeSQLEntity) \
            .filter(RecipeSQLEntity.name == recipe_name) \
            .first()
        if not recipe:
            recipe = RecipeSQLEntity()
            recipe.name = recipe_name
            db.session.add(recipe)
            db.session.commit()

        for column in row[1:]:
            item = db.session.query(ItemSQLEntity) \
                .filter(ItemSQLEntity.name == column) \
                .first()
            if not item:
                item = ItemSQLEntity()
                item.name = column
                db.session.add(item)
                db.session.commit()

            recipe_item = db.session.query(RecipeItemSQLEntity) \
                .filter(RecipeItemSQLEntity.recipeId == recipe.id) \
                .filter(RecipeItemSQLEntity.itemId == item.id) \
                .first()

            if not recipe_item:
                recipe_item = RecipeItemSQLEntity()
                recipe_item.recipeId = recipe.id
                recipe_item.itemId = item.id
                db.session.add(recipe_item)
                db.session.commit()
