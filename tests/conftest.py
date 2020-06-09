from functools import wraps
from typing import Optional

import pytest
from flask import Flask
from flask_login import LoginManager, login_user
from sqlalchemy import orm


from src.infrastructure.database.models import UserItemSQLEntity, UserSQLEntity, ItemSQLEntity
from src.infrastructure.database.models.db import db


def find_user_by_id(user_id: int) -> Optional[UserSQLEntity]:
    return db.session.query(UserSQLEntity).get(user_id)


@pytest.fixture(scope='session')
def app():
    app = Flask(__name__, template_folder='../src/infrastructure/pages')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/eatlist_test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '@##&6cweafhv3426445'
    app.url_map.strict_slashes = False

    login_manager = LoginManager()
    login_manager.init_app(app)
    db.init_app(app)

    app.app_context().push()

    orm.configure_mappers()
    db.create_all()
    db.session.commit()

    @app.route('/test/signin', methods=['POST'])
    def test_signin():
        from flask import request
        identifier = request.get_json().get("identifier")
        user = find_user_by_id(identifier)
        login_user(user, remember=True)
        return '{}', 204

    return app


def truncate_all_tables():
    db.session.query(UserItemSQLEntity).delete()
    db.session.query(UserSQLEntity).delete()
    db.session.query(ItemSQLEntity).delete()
    db.session.flush()


def clean_database(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        db.session.rollback()
        truncate_all_tables()
        return f(*args, **kwargs)

    return decorated_function
