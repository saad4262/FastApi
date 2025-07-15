from fastapi import FastAPI, HTTPException , Request
from fastapi.responses import JSONResponse


app = FastAPI()

items = {"foo": "1"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}





class MyCustomException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(MyCustomException)
def custom_exception_handler(request: Request, exc: MyCustomException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} caused an error."}
    )

@app.get("/error/{name}")
def trigger_error(name: str):
    if name == "bad":
        raise MyCustomException(name)
    return {"name": name}
