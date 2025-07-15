from fastapi import FastAPI
from typing import Union
from enum import Enum
from pydantic import BaseModel

app = FastAPI()


class schema(BaseModel):
    name: str
    roll_no: Union[int, None] = None
    Class: str

class Choice_num(str, Enum):
    one = "one"
    two = "two"
    three = "three"

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def path_func(item_id: int):
    return {"item_id": item_id}

@app.get("/query")
def query_func(name: str, roll_no: Union[int,None] = None): 
    return {"name": name, "roll_no": roll_no}



@app.get("/models/{model_name}")
async def get_model(model_name: Choice_num):
    if model_name is Choice_num.one:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "two":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}



fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    
    return fake_items_db[skip : skip + limit]



@app.post("/items/")
async def create_item(item: schema):
    return item