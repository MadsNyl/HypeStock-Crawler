class Article:
    url: str
    provider: str
    created_date: str

    def __init__(self, url: str, provider: str, created_date: str) -> None:
        self.url = url
        self.provider = provider
        self.created_date = created_date
