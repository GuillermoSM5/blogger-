from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from app.core.database import get_db
from crud.user import create_user
from schemas.response_models import ApiResponse


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post('/', response_model=ApiResponse)
def get_users(user: UserCreate, db: Session = Depends(get_db)):
    create_user(db=db, user=user)
    return ApiResponse(message='El usuario a sido creado exitosamente')
