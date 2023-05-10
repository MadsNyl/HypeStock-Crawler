class INSERT_QUERY:
    @staticmethod
    def article() -> str:
        return """
            INSERT INTO article
            (url, provider)
            VALUES (%s, %s)
        """

    @staticmethod
    def hit() -> str:
        return """
            INSERT INTO article_stock
            (symbol, article_url)
            VALUES (%s, %s)
        """
