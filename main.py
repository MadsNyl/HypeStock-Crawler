from app import Crawler
from util import timer

URLS = [
    "https://edition.cnn.com/business",
    "https://www.nasdaq.com/news-and-insights/markets",
    "https://finance.yahoo.com/topic/stock-market-news/",
    "https://www.cnbc.com/finance/",
    "https://www.ft.com/markets",
]


def main():
    crawlers = [
        # Crawler("https://edition.cnn.com/business", "edition.cnn.com", "cnn"),
        # Crawler("https://www.cnbc.com/finance/", "www.cnbc.com", "cnbc"),
        # Crawler("https://www.nasdaq.com/news-and-insights", "www.nasdaq.com", "nasdaq"),
        Crawler(
            "https://finance.yahoo.com/topic/stock-market-news/",
            "finance.yahoo.com",
            "yahoo",
        ),
        Crawler("https://www.ft.com/markets", "www.ft.com", "ft"),
    ]

    for c in crawlers:
        c.run()


if __name__ == "__main__":
    timer(main)
