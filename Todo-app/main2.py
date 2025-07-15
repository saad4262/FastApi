from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

# Mount the static files directory
# app.mount("/static", StaticFiles(directory="static"), name="static")
# # Set up Jinja2 templates
# templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://saad:pubg12345@cluster0.1anbt.mongodb.net/")

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     docs= conn.company.employee.find({})
#     # for document in docs:
#     #     print(document)
#     # print(docs)
#     new_doc = []
#     for doc in docs:
#         new_doc.append (
#             {
#                 "id": str(doc["_id"]),  
#                 "note": doc["note"],
               
#             }
#         )
#     print("Serving index.html")
#     return templates.TemplateResponse("index.html", {"request": request,"new_doc": new_doc})


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "query": q}