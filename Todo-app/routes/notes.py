from fastapi import APIRouter

from model.notes import Note
from pymongo import MongoClient
from config.db import conn
from schemas.notes import noteEntity, notesEntity
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import HTTPException
from bson import ObjectId
from starlette.datastructures import FormData





note = APIRouter()

templates = Jinja2Templates(directory="templates")



@note.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    docs= conn.company.employee.find({})
    # for document in docs:
    #     print(document)
    # print(docs)
    new_doc = []
    for doc in docs:
        new_doc.append (
            {
                "id": str(doc["_id"]),  
                "title": doc["title"],
                "desc": doc["desc"],
                "importance": doc["importance"],      
            }
        )
    print("Serving index.html")
    return templates.TemplateResponse("index.html", {"request": request,"new_doc": new_doc})

# @note.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "query": q}

# @note.post("/")
# def add_note(note: Note):
#     inserted_note = conn.company.employee.insert_one(dict(note))
#     return noteEntity(inserted_note) 


from fastapi.responses import RedirectResponse

@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    # data = {
    #     "title": form["title"],
    #     "desc": form["desc"],
    #     "importance": True if form.get("importance") == "on" else False
    # }
    note = conn.company.employee.insert_one(formDict)
    return {"Success": True}

