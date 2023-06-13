from db import pool
from db.models import GET_QUERY


class GET:
    
    @staticmethod
    def tickers() -> dict:
        """
        Returns all tickers as a dict.
        """

        try:
            pool.execute(GET_QUERY.tickers())

            return dict.fromkeys(list(map(lambda x: x[0], pool.fetchall())))

        except Exception as e:
            print(f"Fetching all tickers error: {e}")

    @staticmethod
    def urls(provider: str) -> dict:
        """
        Returns all tickers as a dict.
        """

        try:
            pool.execute(GET_QUERY.urls(), (provider,))

            return dict.fromkeys(list(map(lambda x: x[0], pool.fetchall())))

        except Exception as e:
            print(f"Fetching all urls error: {e}")

    @staticmethod
    def providers() -> list:
        """
        Returns all providers as a list.
        """

        try:
            pool.execute(GET_QUERY.providers())

            return pool.fetchall()

        except Exception as e:
            print(f"Fetching providers error: {e}")
