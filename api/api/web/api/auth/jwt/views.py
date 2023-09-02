from fastapi import APIRouter, Depends
from api.library.jwt_verify import jwt_verify

router = APIRouter()

@router.post("/verify")
async def jwt_login_check(result: dict[str, int | str] = Depends(jwt_verify)) -> dict[str, int | str]:
    return result