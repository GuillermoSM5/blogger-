from passlib.context import CryptContext

# Configura CryptContext para usar bcrypt como esquema principal
# 'deprecated="auto"' maneja automáticamente la actualización de hashes más antiguos
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
