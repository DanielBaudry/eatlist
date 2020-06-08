from typing import Dict, Optional

import bcrypt

from src.domain.user import UserRepository
from src.infrastructure.database.models.db import db
from src.infrastructure.database.models.user_sql_entity import UserSQLEntity


def _hash_new_password(cleartext_password: str) -> bytes:
    return bcrypt.hashpw(cleartext_password.encode('utf-8'),
                         bcrypt.gensalt())


class UserRepositorySQL(UserRepository):
    def add_new_user(self, user_info: Dict) -> UserSQLEntity:
        new_user = UserSQLEntity()
        new_user.username = user_info['username']
        new_user.password = _hash_new_password(user_info['password'])
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_user_by_id(self, user_id: int) -> UserSQLEntity:
        user_sql_entity = db.session.query(UserSQLEntity).get(user_id)
        return user_sql_entity

    def get_user_with_credentials(self, username: str, password: str) -> Optional[UserSQLEntity]:
        user = db.session.query(UserSQLEntity).filter(UserSQLEntity.username == username).first()
        if user and bcrypt.hashpw(password.encode('utf-8'), user.password) == user.password:
            return user
        return None
