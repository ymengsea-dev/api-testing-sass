from passlib.context import CryptContext
from app.core.config import SECRET_KEY, TOKEN_EXPIRE_MINUTES, ALGORITHM
from datetime import datetime, timezone, timedelta
import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def generate_access_token(user_id: int, username: str, email: str):
    encode = {
        "sub": str(user_id),
        "username": username,
        "email": email,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=int(TOKEN_EXPIRE_MINUTES)),
    }
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, ALGORITHM)