from typing import TypeVar, Generic, Optional
from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    # status_code: int = status.HTTP_200_OK
    message: str
    data: Optional[T] = None


class ErrorResponse(BaseModel):
    message: str
    detail: Optional[str] = None
