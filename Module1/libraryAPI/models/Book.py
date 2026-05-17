from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Book(Base):
    __tablename__="books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=True)
    is_available = Column(Boolean, default=True)
    
    author = relationship("Author", back_populates="books")
    categories = relationship("Category", secondary="books_categories", back_populates="books")