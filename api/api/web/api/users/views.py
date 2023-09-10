from typing import List
from api.db.dao.user_dao import UserDAO
from api.library.auth import is_authenticated
from api.web.api.users.schema import UserModelDTO
from fastapi import APIRouter, Depends, HTTPException

from api.db.dao.user_follow_dao import FollowDAO

from sqlalchemy.ext.asyncio import AsyncSession
from api.db.dependencies import get_db_session

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


@router.get("/{user_id}/followers", response_model=List[UserModelDTO])
async def get_followers(
    user_id: int,
    follow_dao: FollowDAO = Depends(),
) -> List[UserModelDTO]:
    return await follow_dao.get_user_followers(user_id)



@router.post("/{user_id}/follow")
async def follow_user(
    user_id: int, 
    follow_dao : FollowDAO = Depends(),
    user_info: UserModelDTO = Depends(is_authenticated),
    user_dao: UserDAO = Depends(),
):
    user = await user_dao.get_user(user_id = user_info.id)
    await follow_dao.create_follow(user.id, user_id)
    return {"status": "Followed successfully"}


@router.put("/{user_id}/unfollow")
async def unfollow_user(
    user_id: int, 
    user_info: UserModelDTO = Depends(is_authenticated),
    follow_dao : FollowDAO = Depends(),
    user_dao: UserDAO = Depends(),
):
    user = await user_dao.get_user(user_id = user_info.id)
    await follow_dao.delete_follow(user.id, user_id)
    return {"status": "Unfollowed successfully"}

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

