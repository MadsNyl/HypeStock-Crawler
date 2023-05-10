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
    c = Crawler("https://edition.cnn.com/business", "edition.cnn.com", "cnn")
    c.run()


if __name__ == "__main__":
    timer(main)
