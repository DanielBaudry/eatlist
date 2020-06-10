import bcrypt
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, LargeBinary

from src.infrastructure.database.models.model import Model


class RecipeSQLEntity(Model):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(80), unique=True)
