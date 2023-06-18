from db import pool, db
from db.models import UPDATE_QUERY


class UPDATE():
    
    @staticmethod
    def ticker_article_word(id: int, symbol: str) -> None:
        """
        Updates article_word for ticker.
        """
        try:
            pool.execute(
                UPDATE_QUERY.ticker_article_word(),
                (
                    id,
                    symbol
                )
            )

            db.commit()
        except Exception as e:
            print(f"Updating article word for ticker error: {e}")