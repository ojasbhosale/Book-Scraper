# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, database, scraper
from .models import BookOut, BookCreate

app = FastAPI()

# Create the database tables
@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=database.engine)

# Add a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Scraper API!"}

@app.post("/books/", response_model=BookOut)
def create_book(book_data: BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db=db, book_data=book_data)

@app.get("/books/", response_model=list[BookOut])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    books = crud.get_books(db=db, skip=skip, limit=limit)
    return books

@app.get("/scrape/")
def scrape_and_store_books(db: Session = Depends(database.get_db)):
    books = scraper.scrape_books()
    for book_data in books:
        crud.create_book(db=db, book_data=BookCreate(**book_data))
    return {"message": "Books scraped and stored successfully!"}
