from sqlalchemy.orm import Session
from schemas.user import UserCreate, User
from app.core.security import get_password_hash


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.phrase)
    db_user = User(
        user_name=user.user_name,
        email=user.email,
        phrase=hashed_password
    )
    db.add(db_user)
    db.commit()
    # Actualiza la instancia con los datos de la DB (ej. id, created_at)
    db.refresh(db_user)
    return db_user
