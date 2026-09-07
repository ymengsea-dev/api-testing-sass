from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.api_response import ApiResponse
from app.schemas.user import UserCreate, UserLogin, UserOut, Token
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=ApiResponse[UserOut])
def register(payload: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, payload)

@router.post("/login", response_model=ApiResponse[Token])
def login(payload: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, payload)