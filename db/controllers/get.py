from db import pool
from db.models import GET_QUERY
from classes import Provider


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
    def providers() -> list[Provider]:
        """
        Returns all providers as a list.
        """

        try:
            pool.execute(GET_QUERY.providers())

            providers = pool.fetchall()

            return [
                Provider(
                    provider=provider[0],
                    start_url=provider[1],
                    base_url=provider[2]
                )
                for provider in providers
            ]

        except Exception as e:
            print(f"Fetching providers error: {e}")
    
    @staticmethod
    def provider(name: str) -> Provider:
        """
        Returns a given provider.
        """

        try:
            pool.execute(
                GET_QUERY.provider(),
                (name, )
            )

            provider = pool.fetchone()

            return Provider(
                    provider=provider[0],
                    start_url=provider[1],
                    base_url=provider[2]
                )
                

        except Exception as e:
            print(f"Fetching providers error: {e}")

    @staticmethod
    def article_words() -> dict[str, None]:
        """
        Returns all article_words as a dict.
        """
        try:
            pool.execute(GET_QUERY.article_words())

            return dict.fromkeys(list(map(lambda x: x[0], pool.fetchall())))
        except Exception as e:
            print(f"Fetching article_words error: {e}")
    

    @staticmethod
    def config_url():
        """
        Returns the url of the config.
        """
        try:
            pool.execute(GET_QUERY.config_url(), ("config.json", ))

            return pool.fetchone()[0]
        except Exception as e:
            print(f"Fetching config url error: {e}")