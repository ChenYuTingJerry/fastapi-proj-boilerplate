from abc import abstractmethod, ABCMeta


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
