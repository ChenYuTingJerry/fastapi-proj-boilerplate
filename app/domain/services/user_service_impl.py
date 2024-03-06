from domain.repositories.user_repo import IUserRepository
from domain.services.user_service import IUserService


class UserService(IUserService):

    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    async def get_user(self):
        return await self.user_repo.get_by_id("")

    async def add_user(self):
        pass

    async def remove_user(self):
        pass