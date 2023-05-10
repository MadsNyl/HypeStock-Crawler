from .scraper import Scraper
from collections import deque
from util import is_valid_link, is_sliced_link, is_html, progressbar
from classes import Article, Text
from db import GET, INSERT


class Crawler(Scraper):
    _PROVIDER: str
    _URLS: list[str] = []
    _TICKERS: dict[str]
    _BASE_URL: str
    _START_URL: str

    def __init__(self, start_url: str, base_url: str, provider: str) -> None:
        super().__init__(start_url, base_url)
        self._PROVIDER = provider
        self._TICKERS = GET.tickers()
        self._BASE_URL = base_url
        self._START_URL = start_url
        self._URLS = GET.urls()

    def run(self, cap: int = 500) -> None:
        links = self._crawl(self._START_URL, cap)
        links = self._filter(links)
        self._scrape(links)

    def _filter(self, links: list[str]) -> list[str]:
        filtered_links = []

        for link in links:
            if is_html(link):
                filtered_links.append(link)

        return filtered_links

    def _scrape(self, links: list[str]) -> None:
        progressbar(0, len(links), "Inserting articles: ")
        for i, link in enumerate(links):
            self._process(link)
            progressbar(i + 1, len(links))

    def _process(self, link: str) -> None:
        page = super()._get_html(link)

        if not page:
            return

        body = page.find("body")
        hits = Text(body.text, self._TICKERS).hits
        INSERT.article(Article(url=link, provider=self._PROVIDER, created_date=None))

        for hit in hits:
            INSERT.hit(link, hit)

    def _crawl(self, url: str, cap: int) -> list[str]:
        visited = []
        queue = deque()

        visited.append(url)
        queue.append(url)

        while queue and len(visited) < cap:
            link_node = queue.popleft()

            page = super()._get_html(link_node)
            if page:
                links = super()._get_links(page)
            else:
                links = []

            for link in links:
                if link in self._URLS:
                    continue

                if link not in visited and (
                    is_valid_link(link, self._PROVIDER) or is_sliced_link(link)
                ):
                    if is_sliced_link(link):
                        visited.append(f"https://{self._BASE_URL}{link}")
                        queue.append(f"https://{self._BASE_URL}{link}")
                    else:
                        visited.append(link)
                        queue.append(link)

                    self._URLS[link] = None

        return visited
