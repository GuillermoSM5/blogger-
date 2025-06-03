# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


SQL_ALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQL_ALCHEMY_DATABASE_URL, echo=True)


# Crea una sesión de base de datos
# `autocommit=False` significa que los cambios no se guardan automáticamente
# `autoflush=False` desactiva el vaciado automático de la sesión
# `bind=engine` asocia la sesión con el motor de la base de datos
SessionLocal = sessionmaker(bind=engine)


# Base para los modelos ceclarativos de SQLAlchemy
Base = declarative_base()


def get_db():
    '''
        dependencia para obtener una sesion de base de datos
        estos es crucial para FastApi, ya que permite que cada request tenga su propia session
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
