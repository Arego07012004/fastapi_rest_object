from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    faculty: str | None = None
    course: str | None = None
    grade: str | None = None

class BookOut(BookCreate):
    id: int

    class Config:
        orm_mode = True 
