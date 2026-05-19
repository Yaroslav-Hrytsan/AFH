from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.Author import AuthorCreate, AuthorUpdate
from models.Author import Author
from models.Book import Book

def create_author(db: Session, author: AuthorCreate):
    book_ids = author.books
    books = db.query(Book).filter(Book.id.in_(book_ids)).all()
    new_author = Author(**author.model_dump())
    new_author.books = books
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

def get_authors( db: Session, name: str | None = None):
    all_authors = db.query(Author)
    if name:
        all_authors = all_authors.filter(Author.name.ilike(f"%{name}%"))
    return all_authors.all()

def get_author(db: Session, author_id: int):
    author = db.query(Author).filter(Author.id == author_id).first()
    return author

def update_author(db: Session, author_id: int, author_update: AuthorUpdate):
    # шукаємо автора по id
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        return None
    # беремо тільки ті поля, які реально прийшли в запиті
    update_data = author_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        if key == "books" and value is not None:
            # шукаємо книги по id
            new_books = db.query(Book).filter(Book.id.in_(value)).all()
            author.books = new_books
        else:
            setattr(author, key, value)
    db.commit()
    db.refresh(author)
    return author
    
def delete_author(db:Session, author_id: int):
    author = get_author(db, author_id)
    if not author:
        return None
    active_books = [book for book in author.books if not book.is_available]
    if active_books:
        raise HTTPException(
            status_code = 400, 
            detail = "Can`t delate active book")
    db.delete(author)
    db.commit()
    return author