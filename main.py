import asyncio
from sys import argv
from app import Crawler, Scraper
from classes import Provider, ProxyList, ArticleParser, Article
from db import GET, INSERT
from errors import NoArticlesException
from enums import HTMLTag
from util import timer


PROXY_LIST = ProxyList()
TICKERS = GET.tickers()
URLS = GET.urls()
ARTICLE_WORDS = GET.article_words()

def crawl_articles(provider: Provider, cap: int) -> list[tuple[Provider, str]]:
    crawler = Crawler(
        start_url=provider.start_url,
        base_url=provider.base_url,
        provider=provider.provider,
        tickers=TICKERS,
        urls=URLS
    )

    article_links = crawler.crawl(PROXY_LIST, cap)

    return [
        (provider, link)
        for link in article_links
    ]


async def scrape(article: tuple[Provider, str]) -> None:
    provider = article[0]
    article_link = article[1]

    scraper = Scraper(
        start_url=provider.start_url,
        base_url=provider.base_url
    )

    article_html = await scraper._get_html_async(article_link, PROXY_LIST.proxy)

    if not article_html:
        return
    
    metadata = scraper._get_metadata(article_html)

    article_body = scraper._find(article_html, HTMLTag.BODY.value) 

    if not article_body: 
        return 
    
    article_wrapper = scraper._find_page_text(article_body)

    article_parser = ArticleParser(
        text=article_wrapper.get_text(),
        tickers=TICKERS,
        provider=provider.provider,
        article_words=ARTICLE_WORDS
    )

    tickers = article_parser.get_tickers()

    if not len(tickers):
        return

    article_id = INSERT.article(
        Article(
            url=article_link,
            provider=provider.provider,
            created_date=metadata.created_date,
            title=metadata.title
        )
    )

    if not article_id:
        return
    
    for ticker in tickers:
        INSERT.hit(
            article_id=article_id,
            ticker=ticker
        )

async def scrape_articles(articles: list[tuple[Provider, str]]) -> None:
    await asyncio.gather(*[scrape(article) for article in articles])


def main():
    PROVIDERS = GET.providers()
    cap = 250

    if len(argv) > 1:
        cap = argv[1] 

    articles: list[tuple[Provider, str]] = []
    for provider in PROVIDERS:
        articles += crawl_articles(provider, cap)
    
    if not len(articles):
        raise NoArticlesException("There are no articles to scrape at the moment.")
    
    asyncio.run(scrape_articles(articles))


if __name__ == "__main__":
    timer(main)
