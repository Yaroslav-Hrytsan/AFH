from fastapi import FastAPI
from database import Base, engine 
from routers import Authors, Books, Categories

from database import Base

app = FastAPI(title="Library API", version="1.0.0")

Base.metadata.create_all(bind=engine)

app.include_router(Authors.router)
app.include_router(Books.router)
app.include_router(Categories.router)



