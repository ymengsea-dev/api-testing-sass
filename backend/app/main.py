from fastapi import FastAPI
from app.routers import auth, endpoit, test_case
from app.db.database import Base, engine
from app.core.error_handlers import register_exception_handlers

Base.metadata.create_all(bind=engine)

app = FastAPI()
register_exception_handlers(app)

for module in (auth, endpoit, test_case):
    app.include_router(module.router)