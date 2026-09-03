from fastapi import FastAPI
from app.routers import auth
from app.routers import endpoit
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(endpoit.router)