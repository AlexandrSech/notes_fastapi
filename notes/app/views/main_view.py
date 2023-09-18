from fastapi import APIRouter

from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/health_check")
async def health_check():
    return JSONResponse({"health": True})
