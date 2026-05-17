from fastapi import HTTPException, APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from crud import Categories as crud
from schemas.Category import CategoryCreate, CategoryOut, CategoryUpdate

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[CategoryOut])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@router.get('/{category_id}', response_model=CategoryOut)
def read_category(category_id: int, db: Session = Depends(get_db)):
    return crud.get_category(db, category_id)

@router.post('/', response_model=CategoryOut)
def new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.create_category(db, category)
    return db_category

@router.put('/{category_id}', response_model=CategoryOut)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    db_category = crud.update_category(db, category_id, category)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.delete('/{category_id}', response_model=CategoryOut)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.delete_category(db, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category