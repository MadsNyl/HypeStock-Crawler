import asyncio
from .scraper import Scraper
from collections import deque
from classes import Article, ArticleParser
from db import GET, INSERT
from util import (
    is_valid_link,
    is_sliced_link,
    is_html,
    progressbar,
    is_id_string,
    string_to_datetime,
    build_link,
)


class Crawler(Scraper):
    _PROVIDER: str
    _URLS: dict[str]
    _TICKERS: dict[str]
    _BASE_URL: str
    _START_URL: str

    def __init__(self, start_url: str, base_url: str, provider: str) -> None:
        super().__init__(start_url, base_url)
        self._PROVIDER = provider
        self._TICKERS = GET.tickers()
        self._BASE_URL = base_url
        self._START_URL = start_url
        self._URLS = GET.urls(provider)

    def run(self, cap: int = 500) -> None:
        links = self._crawl(cap)
        asyncio.run(self._process_articles(links))

    async def _process_articles(self, links: list[str]) -> None:
        if not len(links):
            return

        await asyncio.gather(*[self._scrape(link) for link in links])

    async def _scrape(self, url: str) -> None:
        page = await super()._get_html_async(url)

        if not page:
            return

        meta_title = super()._find(page, "meta", property="og:title")
        title = None
        if meta_title:
            title = meta_title.get("content")

        meta_created_date = super()._find(
            page, "meta", property="article:published_time"
        )
        created_date = None
        if meta_created_date:
            created_date = meta_created_date.get("content")
            created_date = string_to_datetime(created_date)

        body = super()._find(page, "body")

        if not body:
            return

        article_parser = ArticleParser(body.text, self._TICKERS, self._PROVIDER)

        if not len(article_parser):
            return

        article_id = INSERT.article(
            Article(
                url=url,
                provider=self._PROVIDER,
                created_date=created_date,
                title=title,
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
            page = super()._get_html(link_node)

            if page:
                links = super()._get_links(page)
            else:
                links = []

            for link in links:
                if is_sliced_link(link):
                    link = build_link(self._BASE_URL, link)

                if link in self._URLS or link in visited:
                    continue

                if (
                    link not in visited
                    and is_valid_link(link, self._PROVIDER)
                    and (is_html(link) or is_id_string(link))
                ):
                    visited.add(link)
                    queue.append(link)
                    self._URLS[link] = None

        return visited
