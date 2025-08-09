from pydantic import BaseModel, Field


class TagCreate(BaseModel):
    name: str = Field(min_length=5, max_length=50,
                      description='Nombre para el tag')


class Tag(BaseModel):
    name: str = None
    id_tag: int = None
