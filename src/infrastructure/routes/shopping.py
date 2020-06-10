from flask import current_app as app, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db
from src.infrastructure.injector import add_item_to_current_list, get_current_shopping_list, \
    remove_item_from_current_shopping_list, get_all_items


@app.route("/list", methods=['GET'])
@login_required
def shopping():
    items = get_all_items.execute()
    shopping_list = get_current_shopping_list.execute(current_user.id)
    return render_template('shopping_list.html',
                           shopping_list=shopping_list.items,
                           items=items)


@app.route("/list/add", methods=['POST'])
@login_required
def add_item():
    add_item_to_current_list.execute(request.form['item'], current_user.id)
    return redirect(url_for('shopping'))


@app.route("/list/remove/<user_item_id>", methods=['GET'])
@login_required
def remove_item(user_item_id: int):
    remove_item_from_current_shopping_list.execute(current_user.id, user_item_id)
    return redirect(url_for('shopping'))
