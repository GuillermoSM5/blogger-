from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.functions import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Post(Base):
    __tablename__ = "posts"

    id_post = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(String(1500), nullable=False)
    image_url = Column(String(255), nullable=True)
    id_autor = Column(Integer, ForeignKey("users.id_user"), nullable=False)
    published = Column(Boolean, default=False)
    minutes_to_read = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())

    autor = relationship("User", back_populates="posts")
