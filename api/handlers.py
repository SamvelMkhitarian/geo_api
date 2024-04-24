from fastapi import HTTPException, status

from api.models import AddressData
from api.query import get_address_data, save_address_data
from api.services import AddressGeoCoder
from sqlalchemy.ext.asyncio import AsyncSession


async def getting_address_handler(address: str, db: AsyncSession) -> AddressData:
    if address_data := await get_address_data(address, db):
        return address_data
    geo = AddressGeoCoder()
    if not (data := await geo.get_data(address)):
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Сервис недоступен',
        )
    if not (address_data := await save_address_data(data, db)):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка базы данных",
        )
    return address_data
