from bs4 import BeautifulSoup
from settings import USER_AGENT
from util import http_get, http_get_async


class Scraper:
    _START_URL: str
    _BASE_URL: str

    def __init__(self, start_url: str, base_url: str) -> None:
        self._START_URL = start_url
        self._BASE_URL = base_url

    def _get_html(self, url: str, proxy: str) -> str:
        try:
            headers = {"User-Agent": USER_AGENT}
            proxies = {"http": f"http://{proxy}"}

            res = http_get(url=url, headers=headers, timeout=2, proxies=proxies)
            return BeautifulSoup(res.text, "html.parser")
        except Exception as e:
            print(f"Fetching url error: {e}")

    async def _get_html_async(self, url: str, proxy: str) -> str:
        try:
            headers = {"User-Agent": USER_AGENT}
            proxies = {"http": f"http://{proxy}"}

            res = await http_get_async(
                url=url, headers=headers, timeout=2, proxies=proxies
            )
            return BeautifulSoup(res.text, "html.parser")
        except Exception as e:
            print(f"Fetching async url error: {e}")

    def _to_html(self, text: str) -> str:
        return BeautifulSoup(text, "html.parser")

    def _get_links(self, page: str) -> list[str]:
        links = page.find_all("a", href=True)
        return list(map(lambda x: x["href"], links))

    def _find(self, soup, tag: str, **kwargs):
        return soup.find(tag, attrs=kwargs)
