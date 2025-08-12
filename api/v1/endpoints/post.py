from fastapi import APIRouter, Depends, status, UploadFile, Form, File, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import cloudinary.uploader
from app.core.database import get_db
from schemas.response_models import ApiResponse
from schemas.post import PostCreate, PostResponse
from crud.post import create_postdb, get_post_byid, get_all_post_db, get_postby_tag


router = APIRouter(
    prefix='/post',
    tags=["Posts"]
)


# @router.post('', response_model=ApiResponse)
@router.post('')
async def create_post(
    file: UploadFile = File(...),
    title: str = Form(..., min_length=5, max_length=255),
    content: str = Form(..., min_length=5, max_length=1500),
    id_autor: int = Form(...),
    tags: list[str] = Form(...),
    db: Session = Depends(get_db)
):
    try:
        upload_result = cloudinary.uploader.upload(file.file)
        image_url_result = upload_result.get("secure_url")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al subir la imagen a Cloudinary: {e}"
        ) from e
    # se tiene que revisar con el navegador
    print(tags)
    if len(tags) > 5:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=ApiResponse(message="Un post no puede tener mas de 5 tags").dict())

    post = PostCreate(title=title, content=content,
                      id_autor=id_autor, tags=tags, image_url=str(image_url_result))

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


@router.get('/bytag/{tag_id}', response_model=ApiResponse[list[PostResponse]])
def get_post_by_tag(tag_id: str, db: Session = Depends(get_db)):
    posts = get_postby_tag(tag_id=tag_id, db=db)
    return ApiResponse(message='Esto son los post por tag', data=posts)
