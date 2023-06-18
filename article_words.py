from util import insert_article_words
from common_uppercase_words import UPPERCASE_WORDS
from classes import ArticleWord

if __name__ == "__main__":
    words: list[ArticleWord] = []

    for word in UPPERCASE_WORDS:
        words.append(
            ArticleWord(
                word=word[0],
                description=word[1]
            )
        )

    insert_article_words(words)