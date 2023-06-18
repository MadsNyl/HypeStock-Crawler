class UPDATE_QUERY:

    @staticmethod
    def ticker_article_word() -> str:
        return """
            UPDATE ticker
            SET article_word = %s
            WHERE symbol = %s
        """