import requests
from bs4 import BeautifulSoup
from settings import USER_AGENT


class Scraper:
    BASE_URL: str

    def __init__(self, base_url: str) -> None:
        self.BASE_URL = base_url

    def _get_html(self, url: str) -> str:
        try:
            res = requests.get(url, timeout=2)
            if res.status_code != 200:
                headers = {"User-Agent": USER_AGENT}
                res = requests.get(url, headers=headers)
                if res.status_code != 200:
                    return None
            return BeautifulSoup(res.text, "html.parser")
        except Exception as e:
            print(e)
            headers = {"User-Agent": USER_AGENT}
            res = requests.get(url, headers=headers)
            return BeautifulSoup(res.text, "html.parser")

    def _get_links(self, page: str) -> list[str]:
        links = page.find_all("a", href=True)
        return list(map(lambda x: x["href"], links))
