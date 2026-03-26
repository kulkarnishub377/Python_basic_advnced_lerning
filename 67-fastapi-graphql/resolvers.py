import strawberry
from typing import List
from schema import Book, Author

# Fake Database
authors_db = [
    Author(id=1, name="George Orwell", country="UK"),
    Author(id=2, name="J.R.R. Tolkien", country="UK")
]

books_db = [
    Book(id=1, title="1984", year=1949, author_id=1),
    Book(id=2, title="Animal Farm", year=1945, author_id=1),
    Book(id=3, title="The Hobbit", year=1937, author_id=2)
]

def get_books() -> List[Book]:
    return books_db

def get_authors() -> List[Author]:
    return authors_db
    
def get_author_by_id(author_id: int) -> Author:
    for a in authors_db:
        if a.id == author_id:
            return a
    return None

def add_book(title: str, year: int, author_id: int) -> Book:
    new_id = len(books_db) + 1
    book = Book(id=new_id, title=title, year=year, author_id=author_id)
    books_db.append(book)
    return book
