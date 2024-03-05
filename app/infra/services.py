
from domain.repositories import UserRepository
from domain.services import UserService


class UserServiceImpl(UserService):

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_user(self):
        return await self.user_repo.get_by_id("")

    async def add_user(self):
        pass

    async def remove_user(self):
        pass
