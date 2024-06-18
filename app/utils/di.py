from fastapi import Depends

from domain.user.repository import IUserRepository
from infra.persistence.user.repo import UserRepository
from services.user_svc import IUserService, UserService


def get_user_service(
    user_repo: IUserRepository = Depends(UserRepository),
) -> IUserService:
    return UserService(user_repo=user_repo)
