from fastapi import APIRouter, Depends
from api.library.jwt_verify import jwt_verify
from api.web.api.auth.jwt.schema import UserModelDTO
from typing import List
router = APIRouter()

# NOTE: この関数はテスト用関数で、削除予定
@router.post("/verify", response_model = UserModelDTO)
async def jwt_login_check(result : UserModelDTO  = Depends(jwt_verify)) -> UserModelDTO :
    return result