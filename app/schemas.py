from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int
    faculty: str | None = None
    course: str | None = None
    grade: str | None = None

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True

