from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse

import injector
from domain.services.user_service import IUserService
from log import logger

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_class=ORJSONResponse)
async def get_user(user_service: IUserService = Depends(injector.get_user_service)):
    logger.info("get_user endpoint")
    return await user_service.get_user()
