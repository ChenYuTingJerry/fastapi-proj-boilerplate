from fastapi import Depends

from domain.repositories.user_repo import IUserRepository
from domain.repositories.user_repo_impl import UserRepository
from domain.services.user_service import IUserService
from domain.services.user_service_impl import UserService


def get_user_service(
    user_repo: IUserRepository = Depends(UserRepository),
) -> IUserService:
    return UserService(user_repo=user_repo)
