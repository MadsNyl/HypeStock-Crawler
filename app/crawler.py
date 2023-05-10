from .scraper import Scraper
from collections import deque
from util import is_valid_link, is_sliced_link, is_html, progressbar, is_id_string
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
            if is_html(link) or is_id_string(link):
                filtered_links.append(link)

        return filtered_links

    def _scrape(self, links: list[str]) -> None:
        if not len(links):
            return
        progressbar(0, len(links), "Inserting articles: ")
        for i, link in enumerate(links):
            self._process(link)
            progressbar(i + 1, len(links))

    def _process(self, link: str) -> None:
        page = super()._get_html(link)

        if not page:
            return

        body = page.find("body")

        if not body:
            return

        hits = Text(body.text, self._TICKERS).hits

        if not len(hits):
            return

        article_id = INSERT.article(
            Article(url=link, provider=self._PROVIDER, created_date=None)
        )

        if not article_id:
            return

        for hit in hits:
            INSERT.hit(article_id, hit)

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

                if is_sliced_link(link):
                    link = f"https://{self._BASE_URL}{link}"

                if link not in visited and is_valid_link(link, self._PROVIDER):
                    visited.append(link)
                    queue.append(link)
                    self._URLS[link] = None

        return visited
