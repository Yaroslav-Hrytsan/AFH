from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    birth_day=Column(String, nullable=True)
    bio=Column(String, nullable=True)

    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")