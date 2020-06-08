from typing import Dict

from src.domain.user import User, UserRepository


class UserSignup:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_info: Dict) -> User:
        return self.user_repository.add_new_user(user_info)