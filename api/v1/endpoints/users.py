from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "User not found"}}
)


@router.get('/')
def get_users():
    return 'Creaste un usuario'
