import re
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
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


async def validation_exception_handler(request: Request, exc: ValidationError):
    print(f"General ValidationError caught: {exc.errors()}")
    errores = []
    for err in exc.errors():
        campo = ".".join(str(loc) for loc in err["loc"])
        print(f"field: {err}")
        errores.append(f"{campo.capitalize()} : {err['msg']}")
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=errores
    )


async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    print(f"General ValidationError caught: {exc.errors()}")
    errores = []
    for err in exc.errors():
        campo = ".".join(str(loc) for loc in err["loc"][1:])
        print(f"field: {err}")
        errores.append(f"{campo.capitalize()} : {err['msg']}")
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=errores
    )


def register_exception_handlers(app):
    app.add_exception_handler(IntegrityError, integrity_error_handler)
    app.add_exception_handler(SQLAlchemyError, sqlalchemy_error_handler)
    app.add_exception_handler(ValidationError,
                              validation_exception_handler)
    app.add_exception_handler(RequestValidationError,
                              request_validation_exception_handler)
