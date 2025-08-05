from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    role: str
    permissions: List[str]


class UserLogin(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    role: str
    permissions: List[str]
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class KBCreate(BaseModel):
    name: str
    role: str


class KBOut(BaseModel):
    id: int
    name: str
    role: str

    class Config:
        from_attributes = True