class GET_QUERY:
    
    @staticmethod
    def tickers() -> str:
        return """
            SELECT symbol
            FROM ticker
        """

    @staticmethod
    def urls() -> str:
        return """
            SELECT url
            FROM article
            WHERE provider = %s
        """

    @staticmethod
    def providers() -> str:
        return """
            SELECT *
            FROM newspaper
        """
