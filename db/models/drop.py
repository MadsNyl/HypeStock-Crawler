class DROP_QUERY:
    
    @staticmethod
    def article_ticker() -> str:
        return """
            DROP TABLE
            article_ticker
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
            newspaper
        """
