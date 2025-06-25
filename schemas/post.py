from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from schemas.user import UserResponse


class PostCreate(BaseModel):
    title: str = Field(min_length=5, max_length=255,
                       description="Titulo para el post")
    content: str = Field(min_length=5, max_length=1500,
                         description="Contenido del post")
    image_url: Optional[str] = Field(description="url de imagen para el post")
    id_autor: int = Field(description="Id del autor del post")


class Post(BaseModel):
    id_post: int = None
    title: str = None
    content: str = None
    image_url: str = None
    id_autor: int = None,
    published: bool = False
    created_at: Optional[datetime] = None
    update_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class PostResponse(BaseModel):
    id_post: int = None
    title: str = None
    content: str = None
    image_url: str = None
    id_autor: int = None,
    published: bool = False
    created_at: Optional[datetime] = None
    update_at: Optional[datetime] = None
    autor: UserResponse

    model_config = ConfigDict(from_attributes=True)
