

from api.library.auth import is_authenticated
from api.web.api.users.schema import UserModelDTO
from fastapi import APIRouter, Depends


router = APIRouter()
@router.get("/me", response_model=UserModelDTO)
async def user_me(
    user_info: UserModelDTO = Depends(is_authenticated),
) -> UserModelDTO:
    return user_info

