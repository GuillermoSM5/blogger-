from sqlalchemy.orm import Session
from schemas.user import UserCreate
from models.user import User, TipoUsuario
from app.core.security import get_password_hash
from app.core.database import SessionLocal


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.phrase)
    db_user = User(
        user_name=user.user_name,
        email=user.email,
        phrase=hashed_password,
        rol=TipoUsuario.LECTOR
    )
    db.add(db_user)
    db.commit()
    # Actualiza la instancia con los datos de la DB (ej. id, created_at)
    db.refresh(db_user)
    return db_user


def get_all_users(db: Session):
    # El offset y el limit estan ahi para el paginado
    result = db.query(User).offset(0).limit(100).all()
    return result


def get_user_byemail(email: str):
    db = SessionLocal()
    usuario = db.query(User).filter(User.email == email).all()
    db.close()
    if not usuario:
        return None
    return usuario[0]
