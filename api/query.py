from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from api.models import AddressData


async def get_address_data(address: str, db: AsyncSession) -> AddressData | None:
    stmt = select(AddressData).where(AddressData.row_address == address)
    res = await db.execute(stmt)
    return res.scalar()


async def save_address_data(data: dict, db: AsyncSession) -> AddressData | None:
    stmt = insert(AddressData).values(**data)
    await db.execute(stmt)
    await db.commit()
    return data
