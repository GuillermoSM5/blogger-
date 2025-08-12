from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from schemas.user import UserResponse
from schemas.tags import Tag


class PostCreate(BaseModel):
    title: str = Field(min_length=5, max_length=255,
                       description="Titulo para el post")
    content: str = Field(min_length=5, max_length=1500,
                         description="Contenido del post")
    image_url: Optional[str] = Field(description="url de imagen para el post")
    id_autor: int = Field(description="Id del autor del post")
    tags: List[str] = []


class Post(BaseModel):
    id_post: int = None
    title: str = None
    content: str = None
    image_url: str = None
    id_autor: int = None,
    published: bool = False
    minutes_to_read: int = None
    slug: str = None
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
    minutes_to_read: int = None
    slug: str = None
    created_at: Optional[datetime] = None
    update_at: Optional[datetime] = None
    autor: UserResponse
    tags: List[Tag] = []

    model_config = ConfigDict(from_attributes=True)
