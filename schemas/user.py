from pydantic import BaseModel, EmailStr, Field
from models.user import TipoUsuario
from datetime import datetime
# Esquema para la creacion de un usuario


class UserCreate(BaseModel):
    user_name: str = Field(
        min_length=5,
        max_length=20,
        description='El nombre de usuario debe tener entre 5 y 20 caracteres.'
    )
    email: EmailStr = Field(
        max_length=50)
    password: str = Field(
        min_length=8,
        max_length=30,
        pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,30}$",
        description="La contraseña debe tener entre 8 y 30 caracteres, al menos una mayúscula, una minúscula, un número y un carácter especial."
    )


class User(BaseModel):
    id_user: int
    user_name: str = Field(max_length=50, min_length=5)
    email: EmailStr
    rol: TipoUsuario = Field("El rol del usuario en el sistema")
    phrase: str
    created_at: datetime
    update_at: datetime
    email_verified: bool
    active: bool

    class ConfigDict:
        from_attributes = True  # Permite que Pydantic lea los atributos de un objeto SQLAlchemy
