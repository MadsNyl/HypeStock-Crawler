class Provider:
    _provider: str
    _start_url: str
    _base_url: str

    def __init__(self, provider: str, start_url: str, base_url: str) -> None:
        self._provider = provider
        self._start_url = start_url
        self._base_url = base_url

    @property
    def provider(self) -> str:
        return self._provider

    @property
    def start_url(self) -> str:
        return self._start_url

    @property
    def base_url(self) -> str:
        return self._base_url
