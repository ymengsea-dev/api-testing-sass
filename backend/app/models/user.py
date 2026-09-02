from sqlalchemy import Column, String, Integer, Uuid
from app.db.database import Base
import uuid

# Defines SQLAlchemy models
class User(Base):
    __tablename__ = "users"
    id = Column(Uuid, primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
    email= Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String, default="user", nullable=False)  # "user" | "admin"