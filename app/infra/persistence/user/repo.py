import uuid

from domain.user.models import User
from domain.user.repository import IUserRepository


class UserRepository(IUserRepository):
    async def get_by_id(self, user_id: str):
        return User(
            user_id=uuid.uuid4(),
            name="jerry",
            age=40,
            email="xxxx@gmail.com",
            gender="male",
        )
