from sqlalchemy import Column, Integer, String
from .database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    age = Column(Integer)
    faculty = Column(String, nullable=True)
    course = Column(String, nullable=True)
    grade = Column(String, nullable=True) 

