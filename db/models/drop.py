class DROP_QUERY:
    @staticmethod
    def article_stock() -> str:
        return """
            DROP TABLE
            article_stock
        """

    @staticmethod
    def article() -> str:
        return """
            DROP TABLE
            article
        """

    @staticmethod
    def provider() -> str:
        return """
            DROP TABLE
            provider
        """
