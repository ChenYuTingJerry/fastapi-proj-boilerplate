from abc import ABCMeta, abstractmethod


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_by_id(self, user_id: str):
        pass
