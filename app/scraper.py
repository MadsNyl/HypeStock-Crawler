from bs4 import BeautifulSoup, NavigableString
from settings import USER_AGENT
from util import http_get, http_get_async, string_to_datetime
from classes import MetaData
from enums import (
    APIJson,
    HTMLAttribute,
    HTMLTag,
    HTMLProperty,
    Parser
)


class Scraper():
    _START_URL: str
    _BASE_URL: str

    def __init__(self, start_url: str, base_url: str) -> None:
        self._START_URL = start_url
        self._BASE_URL = base_url

    def _get_html(self, url: str, proxy: str) -> str:
        try:
            headers = {APIJson.USER_AGENT.value: USER_AGENT}
            proxies = {APIJson.HTTP.value: f"http://{proxy}"}

            res = http_get(url=url, headers=headers, timeout=2, proxies=proxies)
            return BeautifulSoup(res.text, Parser.HTML.value)
        except Exception as e:
            print(f"Fetching url error: {e}")

    async def _get_html_async(self, url: str, proxy: str) -> BeautifulSoup:
        try:
            headers = {APIJson.USER_AGENT.value: USER_AGENT}
            proxies = {APIJson.HTTP.value: f"http://{proxy}"}

            res = await http_get_async(
                url=url, headers=headers, timeout=2, proxies=proxies
            )
            return BeautifulSoup(res.text, Parser.HTML.value)
        except Exception as e:
            print(f"Fetching async url error: {e}")

    def _to_html(self, text: str) -> str:
        return BeautifulSoup(text, Parser.HTML.value)

    def _get_links(self, page: BeautifulSoup) -> list[str]:
        links = page.find_all(HTMLTag.ANCHOR.value, href=True)
        return list(map(lambda x: x[HTMLAttribute.HREF.value], links))

    def _find(self, soup: BeautifulSoup, tag: str, **kwargs) -> NavigableString:
        return soup.find(tag, attrs=kwargs)
    
    def _find_page_text(self, page: NavigableString) -> NavigableString:
        article_wrappers = [
            HTMLTag.ARTICLE.value,
            HTMLTag.SECTION.value
        ]

        for wrapper in article_wrappers:
            new_page = self._find(page, wrapper)
            if new_page:
                return new_page
        
        return page


    def _get_metadata(self, page: NavigableString) -> MetaData:
        meta_title = self._find(page, HTMLTag.META.value, property=HTMLProperty.OG_TITLE.value)
        title = None
        if meta_title:
            title = meta_title.get(HTMLAttribute.CONTENT.value)

        meta_created_date = self._find(page, HTMLTag.META.value, property=HTMLProperty.PUBLISHED_DATE.value)
        created_date = None
        if meta_created_date:
            created_date = meta_created_date.get(HTMLAttribute.CONTENT.value)
            created_date = string_to_datetime(created_date)

        return MetaData(title=title, created_date=created_date)
