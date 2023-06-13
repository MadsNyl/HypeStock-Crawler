from db import CREATE, INSERT
from classes import Provider


INSERT_DATA = [
    Provider("cnn", "https://edition.cnn.com/business", "edition.cnn.com"),
    Provider("cnbc", "https://www.cnbc.com/finance/", "www.cnbc.com"),
    Provider("ft", "https://www.ft.com/markets", "www.ft.com"),
    Provider("yahoo", "https://finance.yahoo.com/topic/stock-market-news/", "finance.yahoo.com")
]

def main() -> None:
    CREATE.up()

    for data in INSERT_DATA:
        INSERT.provider(data)


if __name__ == "__main__":
    main()
