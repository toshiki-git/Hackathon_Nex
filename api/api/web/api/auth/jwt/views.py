from fastapi import APIRouter, Depends

from api.library.is_authenticated import is_authenticated
from api.web.api.users.schema import UserModelDTO

router = APIRouter()

# NOTE: この関数はテスト用関数で、削除予定
@router.get("/verify", response_model=UserModelDTO)
async def jwt_login_check(
    result: UserModelDTO = Depends(is_authenticated),
) -> UserModelDTO:
    return result
