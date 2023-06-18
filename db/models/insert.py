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
            INSERT INTO article_ticker
            (symbol, article_id)
            VALUES (%s, %s)
        """

    @staticmethod
    def provider() -> str:
        return """
            INSERT INTO newspaper 
            (provider, start_url, base_url)
            VALUES (%s, %s, %s)
        """

    @staticmethod
    def article_word() -> str:
        return """
            INSERT INTO article_word
            (word, description)
            VALUES (%s, %s)
        """
