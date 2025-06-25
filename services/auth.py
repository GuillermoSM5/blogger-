from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException, status
from app.core.security import decode_access_token
from crud.user import get_user_byemail
from models.user import TipoUsuario


class BearerJWT(HTTPBearer):
    # def __init__(self, role: list[TipoUsuario] = [TipoUsuario.LECTOR, TipoUsuario.ESCRITOR, TipoUsuario.ADMINISTRADOR], model_data=None):
    #     self.role = role
    #     self.model = model_data

    def __init__(self, role: list[TipoUsuario] = [TipoUsuario.LECTOR, TipoUsuario.ESCRITOR, TipoUsuario.ADMINISTRADOR], bearerFormat=None, scheme_name=None, description=None, auto_error=True):
        super().__init__(bearerFormat=bearerFormat, scheme_name=scheme_name,
                         description=description, auto_error=auto_error)
        self.role = role

    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        email = decode_access_token(auth.credentials)

        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        user = get_user_byemail(email=email)

        if not user.rol in self.role:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        if not user.active:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        return user
