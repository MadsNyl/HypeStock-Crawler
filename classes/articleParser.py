class ArticleParser:
    _text: list[str]
    _hits = set()
    _TICKERS: dict[str]
    _provider: str

    def __init__(self, text: str, tickers: dict[str], provider: str) -> None:
        self._text = self.__strip_parenthesis(text)
        self._TICKERS = tickers
        self._provider = provider
        self.__get_hits()

    def __len__(self) -> int:
        return len(self._hits)

    def __getitem__(self, index) -> str:
        return self._hits[index]

    @property
    def hits(self) -> list[str]:
        return self._hits

    def __get_hits(self) -> None:
        for index, word in enumerate(self._text):
            if self.__is_provider(word):
                continue

            if self.__is_start_of_sentence_pronoun(word, index):
                continue

            if word in self._TICKERS:
                if self.__is_in_uppercase_sentence(index):
                    continue

                self._hits.add(word)

    def __is_in_uppercase_sentence(self, index: int) -> bool:
        if index > 0 and self._text[index - 1].isupper():
            return True

        if index < len(self._text) - 1 and self._text[index + 1].isupper():
            return True

        return False

    def __is_start_of_sentence_pronoun(self, word: str, index: int) -> bool:
        return (
            word.isupper()
            and index > 0
            and self._text[index - 1] == "."
            and len(word) == 1
        )

    def __is_provider(self, word: str) -> bool:
        return word == self._provider.upper()

    def __strip_parenthesis(self, text: str) -> list[str]:
        return list(
            filter(
                lambda x: len(x),
                text.strip().replace("(", " ").replace(")", " ").split(" "),
            )
        )
