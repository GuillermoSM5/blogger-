from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy import Enum
from enum import Enum as PyEnum
from app.core.database import Base


class TipoUsuario(PyEnum):
    ADMINISTRADOR = 'administrador'
    ESCRITOR = 'escritor'
    LECTOR = 'lector'


class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, autoincrement=True, index=True)
    # Se usa String en vez de text para definir una longitud
    user_name = Column(String(50), nullable=False, unique=True, index=True)
    email = Column(String(100), nullable=False, unique=True, index=True)
    rol = Column(Enum(TipoUsuario, name='usuario_enum',
                 length=15), nullable=False)
    phrase = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now)
    update_at = Column(DateTime, default=func.now, onupdate=func.now)
    email_verified = Column(Boolean, default=False)
    active = Column(Boolean, default=True)
