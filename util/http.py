import asyncio
import requests


JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]


def http_get(url: str, **kwargs) -> JSONObject:
    params = kwargs.get("params")
    headers = kwargs.get("headers")
    timeout = kwargs.get("timeout")
    allow_redirects = kwargs.get("allow_redirects")
    data = kwargs.get("data")
    proxies = kwargs.get("proxies")

    return requests.get(
        url,
        params=params,
        headers=headers,
        timeout=timeout,
        allow_redirects=allow_redirects,
        data=data,
        proxies=proxies,
    )


async def http_get_async(url: str, **kwargs) -> JSONObject:
    return await asyncio.to_thread(http_get, url, **kwargs)
