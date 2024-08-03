from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    description: str


class ItemUpdate(BaseModel):
    name: str = None
    description: str = None


class ItemOut(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True
