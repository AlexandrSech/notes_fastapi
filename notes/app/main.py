from fastapi import FastAPI

from app.views.main_view import router as main_router
from app.views.notes import router as note_router
from app.views.boards import router as board_router
from app.models.base import database

app = FastAPI()
app.include_router(main_router)
app.include_router(note_router)
app.include_router(board_router)


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
