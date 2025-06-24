from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException, status
from app.core.security import decode_access_token
from crud.user import get_user_byemail
from models.user import TipoUsuario


class BearerJWT(HTTPBearer):
    def __init__(self, role: list[TipoUsuario] = [TipoUsuario.LECTOR]):
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
