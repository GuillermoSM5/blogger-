from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException, status
from app.core.security import decode_access_token
from crud.user import get_user_byemail


class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        email = decode_access_token(auth.credentials)

        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        user = get_user_byemail(email=email)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        if not user.active:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        return user
