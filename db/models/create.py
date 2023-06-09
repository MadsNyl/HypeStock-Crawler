class CREATE_QUERY:
    
    @staticmethod
    def provider() -> str:
        return """
            CREATE TABLE newspaper(
                provider varchar(255),
                start_url varchar(255),
                base_url varchar(255),
                PRIMARY KEY (provider)
            );
        """

    @staticmethod
    def article() -> str:
        return """
            CREATE TABLE article (
                id int AUTO_INCREMENT,
                title varchar(255),
                url varchar(255),
                provider varchar(255),
                created_date datetime DEFAULT NOW(),
                PRIMARY KEY (id),
                FOREIGN KEY (provider) REFERENCES newspaper (provider),
                UNIQUE(url)
            );
        """

    @staticmethod
    def article_ticker() -> str:
        return """
            CREATE TABLE article_ticker (
                symbol varchar(12),
                article_id int,
                FOREIGN KEY(symbol) REFERENCES ticker(symbol),
                FOREIGN KEY(article_id) REFERENCES article(id)
            );
        """
