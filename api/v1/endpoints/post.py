from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from schemas.response_models import ApiResponse
from schemas.post import PostCreate, PostResponse
from crud.post import create_postdb, get_post_byid, get_all_post_db

router = APIRouter(
    prefix='/post',
    tags=["Posts"]
)


@router.post('', response_model=ApiResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    post = create_postdb(post=post, db=db)
    return ApiResponse(message='El Post ah sido creado exitosamente')


@router.get('/{post_id}', response_model=ApiResponse[PostResponse], name='Get post by id')
def get_postbyid(post_id: str, db: Session = Depends(get_db)):
    post = get_post_byid(post_id=post_id, db=db)
    return ApiResponse(message='Saludos', data=post)


@router.get('', response_model=ApiResponse[list[PostResponse]])
def get_all_post(db: Session = Depends(get_db)):
    post = get_all_post_db(db=db)
    return ApiResponse(message='Obteniendo todo los Post', data=post)
