class GET_QUERY:
    @staticmethod
    def tickers() -> str:
        return """
            SELECT symbol 
            FROM stock
        """

    @staticmethod
    def urls() -> str:
        return """
            SELECT url
            FROM article
            WHERE provider = %s
        """
