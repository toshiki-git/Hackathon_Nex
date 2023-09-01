from fastapi import APIRouter, Depends
from api.library.jwt_verify import jwt_verify
router = APIRouter()

@router.post("/verify")
async def jwt_login_check(result: dict = Depends(jwt_verify)) -> dict:
    return result