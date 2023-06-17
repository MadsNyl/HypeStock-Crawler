from db.models import CREATE_QUERY
from db import pool, db


class CREATE:
    
    @staticmethod
    def up():
        """
        Creates all tables related to articles.
        """

        try:
            pool.execute(CREATE_QUERY.provider())
            db.commit()

            pool.execute(CREATE_QUERY.article())
            db.commit()

            pool.execute(CREATE_QUERY.article_ticker())
            db.commit()

        except Exception as e:
            print(f"Creating tables error: {e}")
