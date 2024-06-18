from abc import abstractmethod, ABCMeta

from domain.user.repository import IUserRepository
from utils.log import logger


class IUserService(metaclass=ABCMeta):
    @abstractmethod
    async def get_user(self):
        pass

    @abstractmethod
    async def add_user(self):
        pass

    @abstractmethod
    async def remove_user(self):
        pass


class UserService(IUserService):
    def __init__(self, user_repo: IUserRepository):
        logger.info("UserService")
        self.user_repo = user_repo

    async def get_user(self):
        return await self.user_repo.get_by_id("")

    async def add_user(self):
        pass

    async def remove_user(self):
        pass
