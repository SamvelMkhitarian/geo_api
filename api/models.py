from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...


class AddressData(Base):
    __tablename__ = "address_data"

    id = Column(Integer, primary_key=True)
    row_address = Column(String)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
