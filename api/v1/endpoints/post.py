from fastapi import APIRouter, Depends, status, UploadFile, Form, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.core.database import get_db
from schemas.response_models import ApiResponse
from schemas.post import PostCreate, PostResponse
from crud.post import create_postdb, get_post_byid, get_all_post_db
import json

router = APIRouter(
    prefix='/post',
    tags=["Posts"]
)


# @router.post('', response_model=ApiResponse)
@router.post('')
async def create_post(file: UploadFile = File(...), data: str = Form(...), db: Session = Depends(get_db)):
    print(file.filename)
    print(data)
    # try:
    parsed_data = json.loads(data)
    item = PostCreate(**parsed_data)
    # except Exception as e:
    #     raise HTTPException(
    #         status_code=422, detail=f"Error de validación: {e}") from e
    # try:
    #     parsed_data = PostCreate(**json.loads(data))
    # except ValidationError as e:
    #     raise HTTPException(status_code=422, detail=e.errors()) from e
    # if len(post.tags) > 5:
    #     return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=ApiResponse(message="Un post no puede tener mas de 5 tags").dict())

    # post = create_postdb(post=post, db=db)
    # return ApiResponse(message='El Post ah sido creado exitosamente')
    return ''


@router.get('/{post_id}', response_model=ApiResponse[PostResponse], name='Get post by id')
def get_postbyid(post_id: str, db: Session = Depends(get_db)):
    post = get_post_byid(post_id=post_id, db=db)
    return ApiResponse(message='Saludos', data=post)


@router.get('', response_model=ApiResponse[list[PostResponse]])
def get_all_post(db: Session = Depends(get_db)):
    post = get_all_post_db(db=db)
    return ApiResponse(message='Obteniendo todo los Post', data=post)
