from abc import abstractmethod, ABC
from typing import Dict

from src.infrastructure.database.models.user_sql_entity import UserSQLEntity


class User:
    def __init__(self, password: str, username: str) -> None:
        self.password = password
        self.username = username


class UserRepository(ABC):
    @abstractmethod
    def add_new_user(self, user_info: Dict) -> UserSQLEntity:
        pass

    @abstractmethod
    def get_user_with_credentials(self, username: str, password: str) -> UserSQLEntity:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> UserSQLEntity:
        pass
