from fastapi import Depends

from domain.repositories import UserRepository
from domain.services import UserService
from infra.repositories import UserRepositoryImpl
from infra.services import UserServiceImpl


def get_user_service(
    user_repo: UserRepository = Depends(UserRepositoryImpl),
) -> UserService:
    return UserServiceImpl(user_repo=user_repo)
