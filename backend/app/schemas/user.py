from pydantic import BaseModel, EmailStr
from uuid import UUID

# Pydantic models for data validation:
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True
        #allow to build obj from a normal 
        #python object attri such as SQLAlchemy model instance.

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserLogin(BaseModel):
    email: EmailStr
    password: str