from fastapi import APIRouter
from schemas.response_models import ApiResponse

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)


@router.post('', response_model=ApiResponse)
def login_user():
    return ApiResponse(message='Este es el login')
