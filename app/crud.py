from sqlalchemy.orm import Session
from app.models import Book

def create_book(db: Session, data):
    book = Book(**data.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_books(db: Session, limit: int, offset: int):
    return db.query(Book).offset(offset).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def delete_book(db: Session, book_id: int) -> bool:
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
        return True
    return False

