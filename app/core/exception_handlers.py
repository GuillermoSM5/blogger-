import re
from fastapi import Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from schemas.response_models import ErrorResponse

# Esto es útil si tus nombres de columnas de DB no son directamente amigables para el usuario
DB_COLUMN_TO_FRIENDLY_NAME = {
    "ix_users_email": "correo electrónico",
    "ix_users_user_name": "nombre de usuario",
}


async def integrity_error_handler(request: Request, exc: IntegrityError):
    print(f"IntegrityError caught: {exc}")
    print(f"Original DB exception: {exc.orig}")

    error_detail = "Error de duplicidad. Un registro con un valor unico ya existe.",

    if exc.orig:
        db_error_message = str(exc.orig)
        if "1062" in db_error_message:
            match = re.search(
                r"Duplicate entry '(.+?)' for key '(\w+\.)?(\w+)'", db_error_message)
            if match:
                print(match)
                duplicated_value = match.group(1)
                db_key = match.group(3)
                error_detail = f"El {DB_COLUMN_TO_FRIENDLY_NAME.get(db_key,db_key)} '{duplicated_value}' ya existe. Por favor elige uno diferente"

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content=ErrorResponse(
            message=error_detail
        ).model_dump()
    )


async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
    print(f"General SQLAlchemyError caught: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(
            message="Ocurrió un error inesperado en la base de datos."
        ).model_dump()
    )


def register_exception_handlers(app):
    app.add_exception_handler(IntegrityError, integrity_error_handler)
    app.add_exception_handler(SQLAlchemyError, sqlalchemy_error_handler)
