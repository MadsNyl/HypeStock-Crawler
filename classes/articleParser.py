from common_uppercase_words import UPPERCASE_WORDS


class ArticleParser:
    _text: list[str]
    _hits = set()
    _TICKERS: dict[str]
    _provider: str

    def __init__(self, text: str, tickers: dict[str], provider: str) -> None:
        self._text = self.__strip_parenthesis(text)
        self._TICKERS = tickers
        self._provider = provider

    def __iter__(self) -> list[str]:
        return iter(self._hits)

    def __len__(self) -> int:
        return len(self._hits)

    def __getitem__(self, index) -> str:
        return self._hits[index]

    def __str__(self) -> str:
        return str(self._hits)

    def get_tickers(self) -> list[str]:
        hits = set()
        for index, word in enumerate(self._text):
            if word in UPPERCASE_WORDS:
                continue

            if word in self._TICKERS:
                if self.__is_provider(word):
                    continue

                if self.__is_in_uppercase_sentence(index):
                    continue

                hits.add(word)
        
        return hits

    def __get_hits(self) -> None:
        for index, word in enumerate(self._text):
            if word in UPPERCASE_WORDS:
                continue

            if word in self._TICKERS:
                if self.__is_provider(word):
                    continue

                if self.__is_in_uppercase_sentence(index):
                    continue

                self._hits.add(word)

    def __is_in_uppercase_sentence(self, index: int) -> bool:
        if index > 0 and self._text[index - 1].isupper():
            return True

        if index < len(self._text) - 1 and self._text[index + 1].isupper():
            return True

        return False

    def __is_provider(self, word: str) -> bool:
        return word == self._provider.upper()

    def __strip_parenthesis(self, text: str) -> list[str]:
        return list(
            filter(
                lambda x: len(x),
                text.strip().replace("(", " ").replace(")", " ").split(" "),
            )
        )
