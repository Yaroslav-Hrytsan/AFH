from sqlalchemy.orm import Session
from schemas.Book import BookCreate, BookUpdate
from models.Book import Book
from models.Category import Category

def create_books(db: Session, book: BookCreate):
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_books(db: Session):
    all_books = db.query(Book).all()
    return all_books

def get_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    return book

def update_book(db: Session, book_id: int, book_update: BookUpdate):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None
    update_data = book_update.model_dump(exclude_unset=True)
    if "categories" in update_data:
        categories_ids = update_data.pop("categories")
        book.categories = db.query(Category).filter(Book.id.in_(categories_ids)).all()
    for key, value in update_data.items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

def change_available(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        book.is_available = not book.is_available 
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book