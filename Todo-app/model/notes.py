from pydantic import BaseModel
from typing import Optional


class Note(BaseModel):
    title: str
    desc: str
    importance: Optional[bool] = None
