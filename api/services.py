from typing import TypedDict
import aiohttp

from api.settings import API_KEY, FORMAT, GEO_URL


class GeoCoderResponseDict(TypedDict):
    """Типизированный словарь ответа геокодера на запрос получения адреса."""

    address: str
    row_address: str
    longitude: float
    latitude: float


class AddressGeoCoder:
    """Сервис геокодера для получения данных по адресу."""

    def __init__(
        self,
        url=GEO_URL,
        api_key=API_KEY,
        format=FORMAT,
    ):
        self.url = url
        self.api_key = api_key
        self.format = format

    async def get_full_address_api(self, address: str) -> aiohttp.ClientResponse:
        """Получение данных по переданному адресу из геокодера."""
        async with aiohttp.ClientSession() as session:
            response = await session.get(
                f'{self.url}?apikey={self.api_key}&geocode={address}&format={self.format}')
            return response

    async def get_data(self, address: str) -> GeoCoderResponseDict | None:
        """Получение и парсинг данных адреса из геокодере."""
        response = await self.get_full_address_api(address)
        data = await response.json()
        if response.status != 200 or data['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found'] == '0':
            return None
        longitude, latitude = map(
            float, data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split())
        full_address = data['response']['GeoObjectCollection']['featureMember'][
            0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']

        return {
            'address': full_address,
            'row_address': address,
            'longitude': longitude,
            'latitude': latitude
        }
