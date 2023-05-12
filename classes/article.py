class Article:
    _url: str
    _provider: str
    _created_date: str
    _title: str

    def __init__(self, url: str, provider: str, created_date: str, title: str) -> None:
        self._url = url
        self._provider = provider
        self._created_date = created_date
        self._title = title

    @property
    def url(self):
        return self._url

    @property
    def provider(self):
        return self._provider

    @property
    def created_date(self):
        return self._created_date

    @property
    def title(self):
        return self._title
