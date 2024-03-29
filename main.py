import asyncio
from app import Crawler, Scraper
from classes import Provider, ProxyList, ArticleParser, Article
from db import GET, INSERT
from errors import NoArticlesException
from enums import HTMLTag
from util import timer, load_config_settings


PROXY_LIST = ProxyList()
TICKERS = GET.tickers()
ARTICLE_WORDS = GET.article_words()

def crawl_articles(provider: Provider, cap: int) -> list[tuple[Provider, str]]:
    crawler = Crawler(
        start_url=provider.start_url,
        base_url=provider.base_url,
        provider=provider.provider,
        tickers=TICKERS,
        urls=GET.urls(provider.provider)
    )

    article_links = crawler.crawl(PROXY_LIST, cap)

    return [
        (provider, link)
        for link in article_links
    ]

def scrape(article: tuple[Provider, str]) -> None:
    provider = article[0]
    article_link = article[1]

    scraper = Scraper(
        start_url=provider.start_url,
        base_url=provider.base_url
    )

    article_html = scraper._get_html(article_link, PROXY_LIST.proxy)

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

async def scrape_async(article: tuple[Provider, str]) -> None:
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
    await asyncio.gather(*[scrape_async(article) for article in articles])


def main():
    PROVIDERS = GET.providers()
    config = load_config_settings()

    cap = 15
    async_scraping = False

    if config:
        cap = config["article"]["limit"]
        async_scraping = config["article"]["async"]


    articles: list[tuple[Provider, str]] = []
    for provider in PROVIDERS:
        articles += crawl_articles(provider, int(cap))
    
    if not len(articles):
        raise NoArticlesException("There are no articles to scrape at the moment.")
    
    if async_scraping:
        asyncio.run(scrape_articles(articles))
    else:
        for article in articles:
            scrape(article)


if __name__ == "__main__":
    timer(main)
