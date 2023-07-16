from db import GET
from sys import argv
from classes import ProxyList, Provider
from app import Crawler

PROXY_LIST = ProxyList()
TICKERS = GET.tickers()

def test(providers: list[Provider]) -> None:
    for provider in providers: 
        articles = crawl_articles(provider)
        print(f"Provider: {provider.provider} - articles: {len(articles)}")

def crawl_articles(provider: Provider, cap: int = 10) -> list[tuple[Provider, str]]:
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

if __name__ == "__main__":

    if len(argv) > 1:
        test([GET.provider(argv[1])])
    else:
        test(GET.providers())