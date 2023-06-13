import asyncio
import requests
from requests import Response


def http_get(url: str, **kwargs) -> Response:
    return requests.get(url, **kwargs)


async def http_get_async(url: str, **kwargs) -> Response:
    return await asyncio.to_thread(http_get, url, **kwargs)
