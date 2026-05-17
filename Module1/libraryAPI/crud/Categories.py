from sqlalchemy.orm import Session
from schemas.Category import CategoryCreate, CategoryUpdate
from models.Category import Category


def get_categories(db: Session):
    all_categories = db.query(Category).all()
    return all_categories

def get_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    return category

def create_category(db: Session, category: CategoryCreate):
    new_category = Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def update_category(db: Session, category_id: int, category_update: CategoryUpdate):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        category.name = category_update.name
        db.commit()
        db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
    return category