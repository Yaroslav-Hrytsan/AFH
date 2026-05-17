from datetime import date
from typing import Optional, List
from pydantic import BaseModel, Field, field_validator
from schemas.Category import CategoryOut
class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    year: int
    author_id: Optional[int]=None
    is_available: bool
    categories: List[int] = Field(default_factory=list)
    @field_validator("title")
    def check_title(cls, title):
        if title == "":
            raise ValueError("Title cannot be empty")
        return title
    @field_validator("year")
    def check_year(cls, year):
        if year > date.today().year:
            raise ValueError("Year cannot be in the future")
        return year
class BookCreate(BookBase):
    pass
    

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    year: Optional[int] = None
    author_id: Optional[int] = None
    is_available: Optional[bool] = None
    categories: Optional[List[int]] = None

class BookAvailable(BaseModel):
    is_available: bool

class BookOut(BookBase):
    id: int
    categories: List[CategoryOut] = Field(default_factory=list)
    class Config:
        from_attributes = True