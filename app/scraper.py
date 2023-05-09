import requests
from bs4 import BeautifulSoup
from settings import USER_AGENT


class Scraper:
    _START_URL: str
    _BASE_URL: str

    def __init__(self, start_url: str, base_url: str) -> None:
        self._START_URL = start_url
        self._BASE_URL = base_url

    def _get_html(self, url: str) -> str:
        try:
            headers = {"User-Agent": USER_AGENT}
            res = requests.get(url, headers=headers, timeout=2)
            return BeautifulSoup(res.text, "html.parser")
        except Exception as e:
            print(f"Fetching url error: {e}")

    def _get_links(self, page: str) -> list[str]:
        links = page.find_all("a", href=True)
        return list(map(lambda x: x["href"], links))
