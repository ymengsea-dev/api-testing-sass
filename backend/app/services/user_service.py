from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_passwor

# Contains business logic separate from API routes

def create_user(db: Session, user: UserCreate):
    new_user = User(username=user.username, password_hash= hash_passwor(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user