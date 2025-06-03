from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "User not found"}}
)


@router.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
def get_users():
    return 'Creaste un usuario'
