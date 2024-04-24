from pydantic import BaseModel, ConfigDict


class GeocodeSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    row_address: str
    address: str
    latitude: float
    longitude: float
