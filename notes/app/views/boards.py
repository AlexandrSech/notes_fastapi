import datetime
from ormar import exceptions
from fastapi import APIRouter, HTTPException

from app.models.board import Board
from app.models.note import Note

router = APIRouter()


@router.get("/board/")
async def board_all():
    return await Board.objects.prefetch_related("notes").all()


@router.get("/board/{board_id}")
async def board_get(board_id: int):
    try:
        return await Board.objects.prefetch_related("notes").filter(id=board_id).get()
    except exceptions.NoMatch:
        raise HTTPException(status_code=404, detail="Item not found")


@router.post("/board/")
async def board_post(board: Board):
    r = await Board(
        name=board.name,
        create_date=datetime.datetime.now(),
        update_date=datetime.datetime.now(),
        notes=board.notes or []
    ).save()
    return r


@router.put("/board/{board_id}")
async def board_update(board_id: int, board: Board):
    item_db = await board_get(board_id)
    if item_db:
        d_4update = {"update_date": datetime.datetime.now()}
        for k, v in board.dict().items():
            if k == "notes" and v:
                d_4update["notes"] = []
                for i in v:
                    r = await Note.objects.filter(pk=i["id"]).all()
                    if r:
                        d_4update["notes"].append(r[0])
            elif v:
                d_4update[k] = v

        await item_db.notes.clear()
        if "notes" in d_4update:
            for note in d_4update["notes"]:
                await item_db.notes.add(note)

        return await item_db.update(**d_4update)
    return None


@router.delete("/board/{board_id}")
async def board_delete(board_id: int, board: Board = None):
    if board:
        return {"deleted_rows": await board.delete()}
    item_db = await board.objects.get(pk=board_id)
    return {"deleted_rows": await item_db.delete()}
