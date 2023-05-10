from db import pool, db
from db.models import INSERT_QUERY
from classes import Article


class INSERT:
    @staticmethod
    def article(article: Article) -> int:
        """
        Inserts an article.
        """
        try:
            pool.execute(INSERT_QUERY.article(), (article.url, article.provider))

            db.commit()

            return pool.lastrowid
        except Exception as e:
            print(f"Inserting article error: {e}")

    @staticmethod
    def hit(article_id: int, ticker: str) -> None:
        """
        Inserts an article and stock in article_stock.
        """
        try:
            pool.execute(INSERT_QUERY.hit(), (ticker, article_id))

            db.commit()
        except Exception as e:
            print(f"Inserting article and stock error: {e}")
