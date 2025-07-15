from typing import Annotated

from fastapi import FastAPI, Form , File, UploadFile

app = FastAPI()



# Form
@app.post("/form/data")
async def formData(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


# File Upload

@app.post("/file/length")
async def fileData(file : bytes = File()):
    return {"file_size": len(file),}

@app.post("/file/upload")
async def uploadFile(file : UploadFile):
    return {"file": file}
