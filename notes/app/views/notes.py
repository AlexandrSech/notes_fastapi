import datetime
from ormar import exceptions
from fastapi import APIRouter, HTTPException

from app.models.note import Note

router = APIRouter()


@router.get("/note/")
async def note_all():
    return await Note.objects.prefetch_related("boards").all()


@router.get("/note/{note_id}")
async def note_get(note_id: int):
    try:
        return await Note.objects.prefetch_related("boards").filter(id=note_id).get()
    except exceptions.NoMatch:
        raise HTTPException(status_code=404, detail="Item not found")


@router.post("/note/")
async def note_post(note: Note):
    r = await Note(
        text=note.text,
        create_date=datetime.datetime.now(),
        update_date=datetime.datetime.now(),
        views=0
    ).save()
    return r


@router.put("/note/{note_id}")
async def note_update(note_id: int, note: Note):
    item_db = await Note.objects.filter(pk=note_id).all()
    if item_db:
        result = await item_db[0].update(text=note.text, update_date=datetime.datetime.now())
        return result
    return None


@router.delete("/note/{note_id}")
async def note_delete(note_id: int, note: Note = None):
    if note:
        return {"deleted_rows": await note.delete()}
    item_db = await Note.objects.get(pk=note_id)
    return {"deleted_rows": await item_db.delete()}
