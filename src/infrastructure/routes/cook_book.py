from flask import render_template, current_app as app
from flask_login import login_required

from src.infrastructure.injector import get_all_recipes


@app.route("/book", methods=['GET'])
@login_required
def cook_books():
    recipes = get_all_recipes.execute()
    return render_template('cook_book.html', recipes=recipes)
