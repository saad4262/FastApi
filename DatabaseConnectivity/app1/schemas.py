from pydantic import BaseModel
from typing import Union

# Item Base
class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

# # User Base
class UserBase(BaseModel):
    # name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    # is_active: bool
    # items: list[Item] = []

    class Config:
        from_attributes = True  # Pydantic v2 preferred
