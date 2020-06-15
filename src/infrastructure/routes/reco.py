from flask import render_template, current_app as app
from flask_login import login_required, current_user

from src.infrastructure.injector import recommend_items


@app.route("/reco", methods=['GET'])
@login_required
def reco():
    items = recommend_items.execute(user_id=current_user.id)
    return render_template(
        'reco.html',
        items=items,
    )
