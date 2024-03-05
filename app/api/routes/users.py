from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse

import injector
from domain.services import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_class=ORJSONResponse)
async def get_user(user_service: UserService = Depends(injector.get_user_service)):
    return await user_service.get_user()
