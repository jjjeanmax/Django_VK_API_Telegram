import aiohttp
from secret import get_secret


async def get_last_sms():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=get_secret(section='TELEGRAM', setting='URL_LAST_SMS')) as response:
            return await response.json()
