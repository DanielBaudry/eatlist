import os
from flask_cors import CORS
from flask import Flask
from flask_login import LoginManager
from flask_admin import Admin
from sqlalchemy import orm

from src.infrastructure.admin.install import install_admin_views
from src.infrastructure.database.models.db import db
from src.infrastructure.injector import get_user_by_id

app = Flask(__name__,
            template_folder='src/infrastructure/pages',
            static_url_path='/static'
            )
app.secret_key = os.environ.get('FLASK_SECRET', 'HZ#1updrH9x6Vs!oQp0tC0!Q')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/eatlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.url_map.strict_slashes = False

admin = Admin(name='Back Office', url='/cook', template_mode='bootstrap3')
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: int):
    return get_user_by_id.execute(user_id)


login_manager.init_app(app)
admin.init_app(app)
db.init_app(app)

cors = CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True
)

with app.app_context():
    import src.infrastructure.routes

    orm.configure_mappers()
    db.create_all()
    db.session.commit()

    install_admin_views(admin=admin, session=db.session)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, use_reloader=True)
