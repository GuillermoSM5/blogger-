from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Tags(Base):
    __tablename__ = "tags"

    id_tag = Column(Integer, primary_key=True,
                    autoincrement=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
