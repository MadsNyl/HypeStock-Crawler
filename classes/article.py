from dataclasses import dataclass


@dataclass
class Article():
    url: str
    provider: str
    created_date: str
    title: str


@dataclass
class ArticleWord():
    word: str
    description: str