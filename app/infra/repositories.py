import uuid

from domain.models import User
from domain.repositories import UserRepository


class UserRepositoryImpl(UserRepository):
    async def get_by_id(self, user_id: str):
        return User(
            user_id=uuid.uuid4(),
            name="jerry",
            age=40,
            email="xxxx@gmail.com",
            gender="male",
        )
