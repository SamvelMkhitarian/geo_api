from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_db
from api.handlers import getting_address_handler
from api.schemas import GeocodeSchema


router = APIRouter()


@router.post("/geocode/", response_model=GeocodeSchema)
async def geocode_address(address: str, db: AsyncSession = Depends(get_db)):
    res = await getting_address_handler(address, db)
    return res
