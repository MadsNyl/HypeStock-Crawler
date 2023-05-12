class INSERT_QUERY:
    @staticmethod
    def article() -> str:
        return """
            INSERT INTO article
            (url, title, provider)
            VALUES (%s, %s, %s)
        """

    @staticmethod
    def article_with_date() -> str:
        return """
            INSERT INTO article
            (url, title, provider, created_date)
            VALUES (%s, %s, %s, %s)
        """

    @staticmethod
    def hit() -> str:
        return """
            INSERT INTO article_stock
            (symbol, article_id)
            VALUES (%s, %s)
        """
