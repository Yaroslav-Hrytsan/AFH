from sqlalchemy.orm import Session
from schemas.Author import AuthorCreate, AuthorUpdate
from models.Author import Author

def get_authors(db: Session):
    all_authors = db.query(Author).all()
    return all_authors

def get_author(db: Session, author_id: int):
    author = db.query(Author).filter(Author.id == author_id).first()
    return author

def create_author(db: Session, author: AuthorCreate):
    new_author = Author(**author.model_dump())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

def update_author(db:Session, author_id: int, author_update: AuthorUpdate):
    author = db.query(Author).filter(Author.id == author_id).first()
    if author:
        author.name = author_update.name
        author.bio = author_update.bio
        author.birth_day = author_update.birth_day
        author.books = author_update.books
        db.commit()
        db.refresh(author)
    return author
    
def delete_author(db:Session, author_id: int):
    author = get_author(db, author_id)
    if author:
        db.delete(author)
        db.commit()
    return author