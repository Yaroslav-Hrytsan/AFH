from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import Authors as crud
from schemas.Author import AuthorUpdate, AuthorCreate, AuthorOut
from database import get_db

router = APIRouter(
    prefix="/authors",
    tags=["authors"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[AuthorOut])
def read_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)

@router.get('/{author_id}', response_model=AuthorOut)
def read_author(author_id: int, db: Session = Depends(get_db)):
    return crud.get_author(db, author_id)

@router.post('/', response_model=AuthorOut)
def new_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = crud.create_author(db, author)
    return db_author

@router.put('/{author_id}', response_model=AuthorOut)
def update_author(author_id: int, author: AuthorUpdate, db: Session = Depends(get_db)):
    db_author = crud.update_authors(db, author_id, author)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@router.delete('/{author_id}', response_model=AuthorOut)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.delete_author(db, author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author
