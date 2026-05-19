from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.Book import BookCreate, BookUpdate
from models.Book import Book
from models.Category import Category

def create_book(db: Session, book: BookCreate):
    # витягуємо id категорій
    category_ids = book.categories
    # шукаємо об’єкти категорій
    categories = db.query(Category).filter(Category.id.in_(category_ids)).all()

    # створюємо книгу без categories
    new_book = Book(
        title=book.title,
        description=book.description,
        year=book.year,
        author_id=book.author_id,
        is_available=book.is_available,
    )

    # додаємо категорії як ORM‑об’єкти
    new_book.categories = categories

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_books(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    title: str | None = None,
    category: str | None = None
):
    query = db.query(Book)
    # пошук по назві
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    # фільтрація по категорії (many-to-many)
    if category:
        query = query.join(Book.categories).filter(Category.name.ilike(f"%{category}%"))
    books = query.offset(skip).limit(limit).all()
    return books

def get_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    return book

def update_book(db: Session, book_id: int, book_update: BookUpdate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        return None

    # перевірка унікальності назви
    if book_update.title:
        existing = db.query(Book).filter(Book.title == book_update.title).first()
        if existing and existing.id != book_id:
            raise HTTPException(status_code=400, detail="Book with this title already exists")

    # оновлення категорій
    if book_update.categories:
        categories = db.query(Category).filter(Category.id.in_(book_update.categories)).all()
        db_book.categories = categories

    # оновлення інших полів
    update_data = book_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book

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