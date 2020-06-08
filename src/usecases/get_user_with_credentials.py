from src.domain.user import UserRepository
from src.infrastructure.database.models import UserSQLEntity


class GetUserWithCredentials:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, username: str, password: str) -> UserSQLEntity:
        return self.user_repository.get_user_with_credentials(username=username, password=password)
