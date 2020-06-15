from flask import current_app as app, render_template, request, redirect, url_for, jsonify
from flask_login import login_required, current_user

from src.infrastructure.injector import add_item_to_current_list, get_shopping_list, \
    remove_item_from_current_shopping_list, get_all_items, archive_current_shopping_list, \
    add_all_recipe_items_to_shopping_list, get_shopping_list_history


@app.route("/list", methods=['GET'])
@login_required
def shopping():
    expected_shopping_list_date = request.args.get('date')
    items = get_all_items.execute()
    history = get_shopping_list_history.execute(current_user.id)
    shopping_list = get_shopping_list.execute(current_user.id, expected_shopping_list_date)
    return render_template(
        'shopping_list.html',
        shopping_list=shopping_list.items,
        shopping_list_history=history.shopping_list_date,
        items=items,
    )


@app.route("/list/archive", methods=['GET'])
@login_required
def archive_shopping_list():
    archive_current_shopping_list.execute(current_user.id)
    return redirect(url_for('shopping'))


@app.route("/list/add", methods=['POST'])
@login_required
def add_item():
    add_item_to_current_list.execute(request.form['item'], current_user.id)
    return jsonify(), 200


@app.route("/list/remove/<user_item_id>", methods=['GET'])
@login_required
def remove_item(user_item_id: int):
    remove_item_from_current_shopping_list.execute(current_user.id, user_item_id)
    return redirect(url_for('shopping'))


@app.route("/list/recipe/add/<recipe_id>", methods=['GET'])
@login_required
def add_recipe(recipe_id: int):
    add_all_recipe_items_to_shopping_list.execute(current_user.id, recipe_id)
    return redirect(url_for('cook_books'))
