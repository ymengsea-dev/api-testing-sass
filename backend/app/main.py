from fastapi import FastAPI
from app.routers import auth
from app.routers import endpoit
from app.db.database import Base, engine
from app.core.error_handlers import register_exception_handlers

Base.metadata.create_all(bind=engine)

app = FastAPI()
register_exception_handlers(app)

app.include_router(auth.router)
app.include_router(endpoit.router)