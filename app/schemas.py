from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    extra: dict

class BookOut(BookCreate):
    id: int

    class Config:
        orm_mode = True 
