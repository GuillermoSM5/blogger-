from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from schemas.response_models import ApiResponse
from schemas.post import PostCreate
from crud.post import create_postdb

router = APIRouter(
    prefix='/post',
    tags=["Posts"]
)


@router.post('', response_model=ApiResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    post = create_postdb(post=post, db=db)
    print(post)
    return ApiResponse(message='El Post ah sido creado exitosamente')
