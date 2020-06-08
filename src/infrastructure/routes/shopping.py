from flask import current_app as app, render_template, request
from flask_login import login_required, current_user

from src.infrastructure.injector import add_item_to_current_list, get_current_shopping_list


@app.route("/list", methods=['GET', 'POST'])
@login_required
def shopping():
    shopping_list = get_current_shopping_list.execute(current_user.id)
    if request.method == 'POST':
        shopping_list = add_item_to_current_list.execute(request.form['item'], current_user.id)
    return render_template('shopping_list.html', shopping_list=shopping_list.items)
