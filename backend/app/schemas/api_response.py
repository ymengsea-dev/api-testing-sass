from typing import Generic, TypeVar, Any
from pydantic import BaseModel

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    success: bool = True
    status: int
    message: str
    data: T | None = None

class ErrorDetail(BaseModel):
    code: str
    details: Any | None = None

class ErrorResponse(BaseModel):
    success: bool = False
    status: int
    message: str
    error: ErrorDetail | None   = None
