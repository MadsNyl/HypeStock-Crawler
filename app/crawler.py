from .scraper import Scraper
from collections import deque
from classes import ProxyList
from util import (
    is_sliced_link,
    build_link,
    is_article,
    is_mail_link,
    is_twitter_link
)


class Crawler(Scraper):
    _PROVIDER: str
    _urls: dict[str]
    _TICKERS: dict[str]
    _BASE_URL: str
    _START_URL: str
    _proxies: ProxyList

    def __init__(self, start_url: str, base_url: str, provider: str, tickers: list[str], urls: list[str]) -> None:
        super().__init__(start_url, base_url)
        self._PROVIDER = provider
        self._TICKERS = tickers
        self._BASE_URL = base_url
        self._START_URL = start_url
        self._urls = urls

    def crawl(self, proxies: ProxyList, cap: int) -> list[str]:
        visited = set()
        queue = deque()

        visited.add(self._START_URL)
        queue.append(self._START_URL)

        while queue and len(visited) < cap:
            link_node = queue.popleft()
            page = super()._get_html(link_node, proxies.proxy)

            links: list[str] = []
            if page:
                links = super()._get_links(page)

            for link in links:
                if (
                    is_mail_link(link) or
                    is_twitter_link(link)
                ):
                    continue

                if is_sliced_link(link):
                    link = build_link(self._BASE_URL, link)

                if link in self._urls or link in visited:
                    continue

                if is_article(
                    visited=visited, link=link, provider=self._PROVIDER, page=page
                ):
                    visited.add(link)
                    queue.append(link)
                    self._urls[link] = None

        visited.discard(self._START_URL)
        return visited
