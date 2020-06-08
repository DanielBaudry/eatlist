from src.domain.user import UserRepository
from src.infrastructure.database.models.user_sql_entity import UserSQLEntity


class GetUserById:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: int) -> UserSQLEntity:
        return self.user_repository.get_user_by_id(user_id=user_id)
