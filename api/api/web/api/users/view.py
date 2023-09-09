
from fastapi import APIRouter, Depends, Request, Response
from fastapi.responses import JSONResponse
from loguru import logger

from api.db.models.user_model import UserModel
from api.api.library.jwt_verify import jwt_verify


router = APIRouter()
logger = logger.bind(task="Users")

@router.get("/users/me")
async def return_user(
    request: Request,
    user: userModel = Depends(jwt_verify),
) -> Response:
    return JSONResponse(
        {
            "user": user_information(
                data = {
                    "user_id": user_model.id,
                    "username": user_model.username,
                    "display_name": user_model.display_name,
                    "is_initialized": user_model.is_initialized,
                    "email": user_model.email,
                },
            ),
        },
    )


@router.patch("/users/me")
async def update_user(
    request: Request,
    user_model: UserModel,
) -> Response:
    user = await user_model.get_user()
    if user is not None:
        return JSONResponse(
            {
                "user": user_information(
                    data = {
                        "user_id": user_model.id,
                        "username": user_model.username,
                        "display_name": user_model.display_name,
                        "is_initialized": user_model.is_initialized,
                        "email": user_model.email,
                    },
                ),
            },
        )
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=json_err_content(
            401,
            "Invalid user_id",
            "Your refresh token is invalid",
        ),
    
    )

