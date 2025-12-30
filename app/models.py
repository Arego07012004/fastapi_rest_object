from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class Book(Base):
     __tablename = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer)
    extra = Column(JSON)
