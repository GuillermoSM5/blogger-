from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict
from models.user import TipoUsuario
import re
# Esquema para la creacion de un usuario

SPECIAL_CHARACTER_REGEX = re.compile(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]")


class UserCreate(BaseModel):
    user_name: str = Field(
        min_length=5,
        max_length=100,
        description='El nombre de usuario debe tener entre 5 y 20 caracteres.'
    )
    email: EmailStr = Field(
        max_length=50)
    phrase: str = Field(
        min_length=8,
        max_length=30,
        description="La contraseña debe tener entre 8 y 30 caracteres, al menos una mayúscula, una minúscula, un número y un carácter especial."
    )

    @field_validator('phrase')  # ¡Cambiamos @validator por @field_validator!
    @classmethod
    def validate_password_strength(cls, value):
        # 1. Validar la longitud primero
        if not (8 <= len(value) <= 30):
            raise ValueError(
                'La contraseña debe tener entre 8 y 30 caracteres.')

        # 2. Validar los requisitos de contenido con expresiones regulares
        # Al menos una minúscula
        if not re.search(r'[a-z]', value):
            raise ValueError(
                'La contraseña debe contener al menos una letra minúscula.')
        # Al menos una mayúscula
        if not re.search(r'[A-Z]', value):
            raise ValueError(
                'La contraseña debe contener al menos una letra mayúscula.')
        # Al menos un número
        if not re.search(r'\d', value):
            raise ValueError('La contraseña debe contener al menos un número.')
        # Al menos un carácter especial (ajusta esta lista según tus necesidades)
        # He incluido los mismos caracteres especiales que en el ejemplo anterior
        special_chars = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]'
        if not re.search(special_chars, value):
            raise ValueError(
                'La contraseña debe contener al menos un carácter especial.')

        return value


class User(BaseModel):
    id_user: Optional[int] = None
    user_name: str = Field(max_length=50, min_length=5)
    email: EmailStr
    rol: TipoUsuario = Field("El rol del usuario en el sistema")
    phrase: str
    created_at: Optional[datetime] = None
    update_at: Optional[datetime] = None
    email_verified: Optional[bool] = False
    active: Optional[bool] = True

    # Permite que Pydantic lea los atributos de un objeto SQLAlchemy
    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    id_user: Optional[int] = None
    user_name: str = Field(max_length=50, min_length=5)
    email: EmailStr
    rol: TipoUsuario = Field("El rol del usuario en el sistema")
    created_at: Optional[datetime] = None
    update_at: Optional[datetime] = None
    email_verified: Optional[bool] = False
    active: Optional[bool] = True

    # Permite que Pydantic lea los atributos de un objeto SQLAlchemy
    model_config = ConfigDict(from_attributes=True)
