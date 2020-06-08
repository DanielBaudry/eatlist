import bcrypt
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, LargeBinary

from src.infrastructure.database.models.model import Model


class UserSQLEntity(Model, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)

    username = Column(String(80), unique=True)

    password = Column(LargeBinary(60), nullable=False)

    def check_password(self, password_to_check: str) -> bool:
        return bcrypt.hashpw(password_to_check.encode('utf-8'), self.password) == self.password
