from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, Token
from app.schemas.api_response import ApiResponse
from app.core.security import hash_password, verify_password, generate_access_token
from fastapi import status
from app.core.exceptions import UserAlreadyExistsError, InvalidCredentialsError

from sqlalchemy.orm import Session

def register_user(db: Session, user: UserCreate):
    if db.query(User).filter(User.email == user.email).first():
        raise UserAlreadyExistsError(field="email")
    
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password),
        role="user"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    response = ApiResponse(
        success= True,
        status= status.HTTP_201_CREATED,
        message = "Register new user successfully",
        data= new_user,
    )

    return response

def login_user(db: Session, data: UserLogin):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise InvalidCredentialsError()
    
    token = Token(access_token=generate_access_token(user.id, user.username, user.email))

    resposne = ApiResponse(
        success = True,
        status= status.HTTP_200_OK,
        message = "Login success",
        data = token,
    )
    return resposne