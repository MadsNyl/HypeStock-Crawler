import asyncio
import requests


JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]


def http_get(url: str, **kwargs) -> JSONObject:
    return requests.get(url, **kwargs)


async def http_get_async(url: str, **kwargs) -> JSONObject:
    return await asyncio.to_thread(http_get, url, **kwargs)
