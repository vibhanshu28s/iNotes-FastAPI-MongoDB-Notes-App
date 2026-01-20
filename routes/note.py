from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


note = APIRouter()
templates = Jinja2Templates(directory="templates")
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "Id": str(doc["_id"]),
            "title": doc.get("title", "No Title"),
            "desc": doc.get("desc", "No Description")
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/")
async def creat_item(request: Request):
    form = await request.form()
    conn.notes.notes.insert_one(dict(form))
    return {"Success" : True}
