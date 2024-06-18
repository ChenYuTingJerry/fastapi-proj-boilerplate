from abc import ABCMeta, abstractmethod


class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_by_id(self, user_id: str):
        pass
