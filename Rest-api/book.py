from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID
from typing import List
from fastapi.exceptions import HTTPException




app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=500)
    rating: int = Field(ge=1, lt=101)

Books = []    


# @app.get("/")
# def root():
#     return {"message": "Welcome to the Book API!"}


@app.get("/")
def read_api():
    return Books




@app.post("/")
def create_book(book: Book):
    Books.append(book)
    return book


@app.put("/{book_id}")
def  update_book(book_id: UUID, book: Book):
    
    counter = 0
    for x in Books:
        if x.id == book_id:
            Books[counter-1] = book
            return Books[counter-1]
    raise HTTPException(
        status_code=404, detail="Book not found"
        )
  

@app.delete("/{book_id}")
def delete_book(book_id: UUID):
        counter = 0
        for x in Books:
            if x.id == book_id:
                del Books[counter-1]
                return f"ID : {book_id} deleted successfully"

        raise HTTPException(
        status_code=404, detail=f"ID {book_id} : Does not Exist"
        )
