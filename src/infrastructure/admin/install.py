from src.infrastructure.admin.custom_views import ItemAdminView, RecipeAdminView
from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.recipe_sql_entity import RecipeSQLEntity


def install_admin_views(admin, session):
    admin.add_view(ItemAdminView(ItemSQLEntity, session, name='Items'))
    admin.add_view(RecipeAdminView(RecipeSQLEntity, session, name='Recettes'))
