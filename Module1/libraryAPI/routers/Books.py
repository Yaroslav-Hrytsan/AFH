from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import Books as crud
from schemas.Book import BookUpdate, BookCreate, BookOut
from database import get_db

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[BookOut])
def read_books(db: Session = Depends(get_db), skip: int = 0,
    limit: int = 10,
    title: str | None = None,
    category: str | None = None):
    return crud.get_books(db, skip=skip, limit=limit, title=title, category=category)

@router.get("/{book_id}", response_model=BookOut)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.post("/", response_model=BookOut)
def new_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@router.put('/{book_id}', response_model=BookOut)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, book_id, book)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put('/{book_id}/available', response_model=BookOut)
def change_available(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.change_available(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete('/{book_id}', response_model=BookOut)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book