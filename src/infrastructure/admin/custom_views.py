from src.infrastructure.admin.base_configuration import BaseAdminView


class ItemAdminView(BaseAdminView):
    can_create = True
    can_edit = True
    can_delete = True
    column_list = ['id', 'name']
    column_labels = dict(id='Id', name='Nom')
    column_searchable_list = ['name']


class RecipeAdminView(BaseAdminView):
    can_create = True
    can_edit = True
    can_delete = True
    column_list = ['id', 'name', 'items']
    column_labels = dict(id='Id', name='Nom', items='Items')
    column_searchable_list = ['name']
