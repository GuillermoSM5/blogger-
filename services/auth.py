from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer
from fastapi import Request
from crud.user import get_user_byemail
from fastapi import Depends, HTTPException, status
from app.core.security import verify_password


def authenticate_user(email: str, phrase: str, db: Session):
    user = get_user_byemail(db=db, email=email)
    if not user:
        return None
    if not verify_password(phrase, hashed_password=user[0].phrase):
        return None
    return user[0]


class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request, db: Session):
        auth = await super().__call__(request)
        # email = decode_access_token(auth.credentials)
        # if email is None:
        # raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        # user = get_user_byemail(email=email, db=db)
        # if user is None:
        #     # raise credential_exception
        #     print('user is none')
        # if not user[0].active:
        #     # raise credential_exceptio
        #     print('user is not active')
        # return user
