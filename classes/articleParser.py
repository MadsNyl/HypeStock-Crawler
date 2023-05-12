class ArticleParser:
    _text: list[str]
    _hits: list[str]
    _TICKERS: dict[str]

    def __init__(self, text: str, tickers: dict[str]) -> None:
        self._text = self._strip_parenthesis(text)
        self._TICKERS = tickers
        self._hits = self._get_hits()

    @property
    def hits(self) -> list[str]:
        return self._hits

    def _get_hits(self) -> list[str]:
        hits: str = []

        # TODO: check for providers
        for word in self._text:
            if word in hits:
                continue

            if word in self._TICKERS:
                hits.append(word)

        return hits

    def _strip_parenthesis(self, text: str) -> list[str]:
        return list(
            filter(
                lambda x: len(x),
                text.strip().replace("(", " ").replace(")", " ").split(" "),
            )
        )
