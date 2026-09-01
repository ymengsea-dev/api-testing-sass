from pydantic import BaseModel

# Pydantic models for data validation:
class UserCreate(BaseModel):
    username: str
    password: str