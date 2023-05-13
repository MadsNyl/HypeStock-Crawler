from db import CREATE, INSERT
from classes import Provider


def main() -> None:
    CREATE.up()
    INSERT.provider(
        Provider("cnn", "https://edition.cnn.com/business", "edition.cnn.com")
    )
    INSERT.provider(Provider("cnbc", "https://www.cnbc.com/finance/", "www.cnbc.com"))
    INSERT.provider(Provider("ft", "https://www.ft.com/markets", "www.ft.com"))
    INSERT.provider(
        Provider(
            "yahoo",
            "https://finance.yahoo.com/topic/stock-market-news/",
            "finance.yahoo.com",
        )
    )


if __name__ == "__main__":
    main()
