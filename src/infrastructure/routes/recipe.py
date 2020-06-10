from flask import render_template, current_app as app
from flask_login import login_required, current_user

from src.infrastructure.injector import get_available_recipes


@app.route("/recipe", methods=['GET'])
@login_required
def recipe():
    recipes = get_available_recipes.execute(current_user.id)
    return render_template('recipe.html', recipes=recipes)
