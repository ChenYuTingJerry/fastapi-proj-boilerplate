from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse

from utils import di
from utils.log import logger
from services.user_svc import IUserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_class=ORJSONResponse)
async def get_user(user_service: IUserService = Depends(di.get_user_service)):
    logger.info("get_user endpoint")
    return await user_service.get_user()
