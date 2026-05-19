from typing import List, Optional
from pydantic import BaseModel, Field
from schemas.Book import BookOut
class AuthorBase(BaseModel):
    name: str
    birth_day: Optional[str] = None
    bio: Optional[str] = None
    books: Optional[List[int]] = Field(default_factory=list)

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(BaseModel):
    name: Optional[str] = None
    books: Optional[List[int]] = None

class AuthorOut(AuthorBase):
    id: int
    books: Optional[List[BookOut]] = Field(default_factory=list)

    class Config:
        from_attributes = True