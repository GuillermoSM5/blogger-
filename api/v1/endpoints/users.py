from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserResponse
from app.core.database import get_db
from crud.user import create_user, get_all_users
from schemas.response_models import ApiResponse
from services.auth import BearerJWT


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post('/', response_model=ApiResponse)
def create_users(user: UserCreate, db: Session = Depends(get_db)):
    create_user(db=db, user=user)
    return ApiResponse(message='El usuario a sido creado exitosamente')


@router.get('/', response_model=ApiResponse[List[UserResponse]], dependencies=[Depends(BearerJWT())])
def get_users(db: Session = Depends(get_db)):
    users = get_all_users(db=db)
    return ApiResponse(message='Obteniendo todo los usuarios', data=users)
