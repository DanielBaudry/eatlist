from flask import url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from werkzeug.utils import redirect


class BaseAdminView(ModelView):
    page_size = 25
    can_set_page_size = True
    can_create = False
    can_edit = False
    can_delete = False

    def is_accessible(self) -> bool:
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin.index'))
