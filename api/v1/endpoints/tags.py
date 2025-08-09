from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from schemas.response_models import ApiResponse
from schemas.tags import TagCreate, Tag
from crud.tags import get_all_tags_db, create_tag_db

router = APIRouter(
    prefix='/tags',
    tags=["Tags"]
)


@router.get('', response_model=ApiResponse[list[Tag]])
def get_all_tags(db: Session = Depends(get_db)):
    tags = get_all_tags_db(db=db)
    return ApiResponse(message='Esto son todos los Tags', data=tags)


@router.post('', response_model=ApiResponse)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    create_tag_db(tag=tag, db=db)
    return ApiResponse(message='Tag Creado correctamente')
