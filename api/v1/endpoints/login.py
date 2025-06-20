from datetime import timedelta
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from schemas.response_models import ApiResponse, ErrorResponse
from schemas.login import LoginUser
from crud.user import get_user_byemail
from app.core.security import verify_password, create_acces_token
from app.core.config import settings

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)


@router.post('', response_model=ApiResponse)
def login_user(user: LoginUser):
    response = JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=ErrorResponse(
        message='Tu contrasena o tu usario son incorrectos').model_dump())
    current_user = get_user_byemail(user.email)
    if current_user is None:
        return response
    if not verify_password(plain_password=user.phrase, hashed_password=current_user.phrase):
        return response
    access_token_expires = timedelta(
        minutes=settings.ACCES_TOKEN_EXPIRE_MINUTES)
    current_token = create_acces_token(
        {"email": current_user.email}, expires_delta=access_token_expires)
    return ApiResponse(message='Este es el login', data=current_token)
