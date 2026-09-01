# contain shared dependencies like db sessions cross the app 
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
        # yaid return one at a time instead of returing everything at once
    finally:
        db.close()