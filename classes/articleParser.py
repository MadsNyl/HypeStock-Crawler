class ArticleParser:
    _text: list[str]
    _hits = set()
    _TICKERS: dict[str]
    _provider: str

    def __init__(self, text: str, tickers: dict[str], provider: str) -> None:
        self._text = self._strip_parenthesis(text)
        self._TICKERS = tickers
        self._provider = provider
        self._get_hits()

    def __len__(self) -> int:
        return len(self._hits)

    def __getitem__(self, index) -> str:
        return self._hits[index]

    @property
    def hits(self) -> list[str]:
        return self._hits

    def _get_hits(self) -> None:
        for word in self._text:
            if self._is_provider(word):
                continue

            if word in self._TICKERS:
                self._hits.add(word)

    def _is_provider(self, word: str) -> bool:
        return word == self._provider.upper()

    def _strip_parenthesis(self, text: str) -> list[str]:
        return list(
            filter(
                lambda x: len(x),
                text.strip().replace("(", " ").replace(")", " ").split(" "),
            )
        )
