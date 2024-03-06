import uuid

from domain.models.user import User
from domain.repositories.user_repo import IUserRepository


class UserRepository(IUserRepository):
    async def get_by_id(self, user_id: str):
        return User(
            user_id=uuid.uuid4(),
            name="jerry",
            age=40,
            email="xxxx@gmail.com",
            gender="male",
        )
