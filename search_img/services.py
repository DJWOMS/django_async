import asyncio
import httpx
import aiofiles

from config.settings import BASE_DIR
from .models import Image


async def get_link(query: str, current_page: int):
    headers = {'Authorization': '563492ad6f91700001000001df3b54e89606406bbb9bd8a521524d74'}
    params = {'query': query, 'per_page': 1, 'page': current_page}
    url = 'https://api.pexels.com/v1/search'

    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers, params=params)
        if res.status_code == 200:
            response = res.json()
            return response.get('photos')[0].get('src').get('original')


async def search_image(query: str, count: int):
    current_page = 0
    images = await asyncio.gather(
        *(get_link(query, count) for count in range(current_page, count)),
        return_exceptions=True
    )
    return images


async def download_file(user_id: int, url: str, query: str):
    async with httpx.AsyncClient() as client:
        file_name = f"media/{user_id}/{url.split('/')[-1]}"
        print(file_name, user_id)
        res = await client.get(url)
        async with aiofiles.open(file_name, 'wb+') as f:
            await f.write(res.read())

    await Image.objects.acreate(title=query, url=file_name, user_id=user_id)


async def save_images(user_id: int, query: str, count: int):
    link_images = await search_image(query, count)
    await asyncio.gather(
        *(download_file(user_id, url, query) for url in link_images),
        return_exceptions=True
    )
    return link_images






