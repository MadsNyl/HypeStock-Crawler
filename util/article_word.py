from db import INSERT, UPDATE
from classes import ArticleWord


def insert_article_words(words: list[ArticleWord]) -> None:
    for word in words:
        insert_id = INSERT.article_word(word)
        UPDATE.ticker_article_word(insert_id, word.word)

