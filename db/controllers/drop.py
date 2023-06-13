from db import pool, db
from db.models import DROP_QUERY


class DROP:
    
    @staticmethod
    def down() -> None:
        """
        Drops all tables related to articles.
        """

        try:
            pool.execute(DROP_QUERY.article_stock())
            db.commit()

            pool.execute(DROP_QUERY.article())
            db.commit()

            pool.execute(DROP_QUERY.provider())
            db.commit()

        except Exception as e:
            print(f"Dropping tables error: {e}")
