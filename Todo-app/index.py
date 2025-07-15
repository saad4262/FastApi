from fastapi import FastAPI, Request
from routes.notes import note
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")




# app.include_router(note, prefix="/notes", tags=["notes"]) 
app.include_router(note) 