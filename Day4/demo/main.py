from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()  #Creates FastAPI app

# Creates Data Model
class Book(BaseModel):
    id: int
    title: str
    author: str

# Creates Fake DB
books : List[Book] = [
    Book(id=1, title='Berserk', author='Miura'),
    Book(id=2, title='Hitchikers Guide', author='Adams')
]

# Create Root Endpoint
@app.get("/")
def read_root():
    return{"Message": "Welcome to the library API"}

# Create a get all books - Endpoint
@app.get("/books", response_model=List[Book])
def get_books():
    return books
