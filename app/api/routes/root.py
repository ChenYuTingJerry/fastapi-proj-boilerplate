from fastapi import APIRouter

router = APIRouter(prefix="", tags=["root"])


@router.get("/health")
async def health():
    return "ok"
