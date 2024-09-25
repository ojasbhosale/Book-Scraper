# app/crud.py
from sqlalchemy.orm import Session
from .models import Book, BookCreate

def create_book(db: Session, book_data: BookCreate):
    db_book = Book(**book_data.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()
