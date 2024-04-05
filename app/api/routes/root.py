from fastapi import APIRouter

router = APIRouter(prefix="", tags=["root"])


@router.get("/")
async def health():
    return "ok"
