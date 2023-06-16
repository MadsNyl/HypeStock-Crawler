import asyncio
from .scraper import Scraper
from collections import deque
from classes import ArticleParser, ProxyList, Article
from db import GET, INSERT
from enums import HTMLTag
from util import (
    is_sliced_link,
    build_link,
    is_article,
    is_mail_link
)


class Crawler(Scraper):
    _PROVIDER: str
    _URLS: dict[str]
    _TICKERS: dict[str]
    _BASE_URL: str
    _START_URL: str
    _proxies: ProxyList

    def __init__(self, start_url: str, base_url: str, provider: str) -> None:
        super().__init__(start_url, base_url)
        self._PROVIDER = provider
        self._TICKERS = GET.tickers()
        self._BASE_URL = base_url
        self._START_URL = start_url
        self._URLS = GET.urls(provider)
        self._proxies = ProxyList()

    def run(self, cap: int = 100) -> None:
        links = self._crawl(cap)
        asyncio.run(self._process_articles(links))

    async def _process_articles(self, links: list[str]) -> None:
        if not len(links):
            return

        await asyncio.gather(*[self._scrape(link) for link in links])

    async def _scrape(self, url: str) -> None:
        page = await super()._get_html_async(url, self._proxies.proxy)
        self._proxies.next()

        if not page:
            return

        metadata = super()._get_metadata(page)

        body = super()._find(page, HTMLTag.BODY.value)

        if not body:
            return

        article_parser = ArticleParser(body.text, self._TICKERS, self._PROVIDER)

        if not len(article_parser):
            return

        article_id = INSERT.article(
            Article(
                url=url,
                provider=self._PROVIDER,
                created_date=metadata.created_date,
                title=metadata.title,
            )
        )

        if not article_id:
            return

        for hit in article_parser:
            INSERT.hit(article_id, hit)

    def _crawl(self, cap: int) -> list[str]:
        visited = set()
        queue = deque()

        visited.add(self._START_URL)
        queue.append(self._START_URL)

        while queue and len(visited) < cap:
            link_node = queue.popleft()
            page = super()._get_html(link_node, self._proxies.proxy)
            self._proxies.next()

            links: list[str] = []
            if page:
                links = super()._get_links(page)

            for link in links:
                if is_mail_link(link):
                    continue

                if is_sliced_link(link):
                    link = build_link(self._BASE_URL, link)

                if link in self._URLS or link in visited:
                    continue

                if is_article(
                    visited=visited, link=link, provider=self._PROVIDER, page=page
                ):
                    visited.add(link)
                    queue.append(link)
                    self._URLS[link] = None

        visited.discard(self._START_URL)
        return visited
