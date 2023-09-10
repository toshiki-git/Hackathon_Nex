

from api.db.dao.user_dao import UserDAO
from api.library.auth import is_authenticated
from api.web.api.users.schema import UserModelDTO, UpdateUserModelDTO
from fastapi import APIRouter, Depends


router = APIRouter()
@router.get("/me", response_model=UserModelDTO)
async def user_me(
    user_info: UserModelDTO = Depends(is_authenticated),
) -> UserModelDTO:
    return user_info

@router.patch("/me")
async def update_user(
    user_update_dto: UpdateUserModelDTO,
    user_info: UserModelDTO = Depends(is_authenticated),
    user_dao: UserDAO = Depends(),
):
    print(dict(user_update_dto))
    user = await user_dao.get_user(user_id=user_info.id)
    user.update_info(data=user_update_dto.model_dump())

    return {"detail": "successfully updated."}
