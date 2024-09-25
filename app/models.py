# app/models.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from .database import Base

# SQLAlchemy Model
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(Float)
    availability = Column(String)
    rating = Column(String)
    product_url = Column(String)

# Pydantic Schema
class BookCreate(BaseModel):
    title: str
    price: float
    availability: str
    rating: str
    product_url: str

class BookOut(BookCreate):
    id: int

    class Config:
        orm_mode = True
