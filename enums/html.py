from enum import Enum


class HTMLTag(Enum):
    META = "meta"
    ARTICLE = "article"
    SECTION = "section"
    DIV = "div"
    ANCHOR = "a"
    BODY = "body"
    TITLE = "title"


class HTMLProperty(Enum):
    OG_TITLE = "og:title"
    PUBLISHED_DATE = "article:published_time"


class HTMLKeyword(Enum):
    MAILTO = "mailto"
    BACKSLASH = "/"
    DOT_HTML = ".html"
    DOT_HTM = ".htm"
    TWITTER = "https://twitter.com"


class HTMLAttribute(Enum):
    HREF = "href"
    CONTENT = "content"