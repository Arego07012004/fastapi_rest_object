from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import Base, engine, SessionLocal
from app import schemas, crud


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=schemas.BookOut)
def create(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books/")
def list_books(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    return crud.get_books(db, limit, offset)

@app.get("/books/{book_id}")
def read(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

