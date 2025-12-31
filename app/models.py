from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Faculty(Base):
    __tablename__ = "faculties"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    courses = relationship("Course", back_populates="faculty")
    students = relationship("Student", back_populates="faculty")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    faculty_id = Column(Integer, ForeignKey("faculties.id"))
    faculty = relationship("Faculty", back_populates="courses")
    students = relationship("Student", back_populates="course")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    age = Column(Integer)
    faculty_id = Column(Integer, ForeignKey("faculties.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))

    faculty = relationship("Faculty", back_populates="students")
    course = relationship("Course", back_populates="students")

