from fastapi import APIRouter, Depends
from api.db.dao.community_dao import CommunityDao
from api.web.api.community.schema import CommunityDTO
from api.db.models.community_model import CommunityModel
from typing import List

router = APIRouter()

@router.post("/")
async def create_community_post(
    dto:CommunityDTO,
    community_dao: CommunityDao = Depends(),
)->None:
    await community_dao.create_community(dto.user_id, dto.community_id, dto.content)
    
@router.get("/", response_model=List[CommunityDTO])
async def get_communities_by_community_id(
    community_id: int,
    community_dao: CommunityDao = Depends(),
)->List[CommunityModel]:
    communities = await community_dao.get_communities_by_community_id(community_id)
    return communities

    
