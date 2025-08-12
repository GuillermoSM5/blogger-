from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

# Tabla de unión para la relación muchos a muchos
# Se define como un objeto Table, no como una clase de modelo
post_tag = Table(
    'post_tag',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id_post'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id_tag'), primary_key=True)
)


class Tags(Base):
    __tablename__ = "tags"

    id_tag = Column(Integer, primary_key=True,
                    autoincrement=True, index=True)
    name = Column(String(50), nullable=False, unique=True)

    posts = relationship(
        "Post",
        secondary=post_tag,
        back_populates="tags"
    )
