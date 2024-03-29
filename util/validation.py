import re
from datetime import datetime
from bs4 import BeautifulSoup
from enums import (
    HTMLKeyword,
    HTMLProperty,
    HTMLTag,
    Pattern,
    DateForamt
)


COMMON_HTML_TAGS = [
    HTMLTag.ARTICLE.value,
    HTMLTag.SECTION.value,
    HTMLTag.DIV.value
]


def is_valid_link(link: str, key: str) -> bool:
    return key.lower() in link.lower()


def is_mail_link(link: str) -> bool:
    return link.startswith(HTMLKeyword.MAILTO.value)


def is_twitter_link(link: str) -> bool:
    return link.startswith(HTMLKeyword.TWITTER.value)


def is_sliced_link(link: str) -> bool:
    return link.startswith(HTMLKeyword.BACKSLASH.value)


def is_html(link: str) -> bool:
    return (
        link.endswith(HTMLKeyword.DOT_HTML.value) or 
        link.endswith(HTMLKeyword.DOT_HTM.value)
    )


def is_id_string(link: str) -> bool:
    return bool(
        re.search(
            Pattern.ID_STRING.value,
            link
        )
    )

def is_hyphen_string(link: str) -> bool:
    return bool(
        re.search(
            Pattern.HYPHEN_STRING.value,
            link
        )
    )

def is_paywall(page: BeautifulSoup) -> bool:
    pattern = re.compile(Pattern.SIGNUP.value, re.IGNORECASE)
    tags = page.find_all(HTMLTag.ANCHOR.value, href=pattern)
    if tags:
        return True
    return False


def is_missing_title(page: BeautifulSoup) -> bool:
    title = page.find(
        HTMLTag.META.value,
        property=HTMLProperty.OG_TITLE.value
    )
    if title:
        return False
    
    title_tag = page.find(
        HTMLTag.TITLE.value
    )
    if title_tag:
        return False
    
    return True


def is_article(visited: set, link: str, provider: str, page: BeautifulSoup) -> bool:
    if link in visited:
        return False

    if not is_valid_link(link, provider):
        return False
    
    if (
        not is_html(link) and 
        not is_id_string(link) and
        not is_hyphen_string(link)
    ):
        return False
    
    if is_missing_title(page):
        return False
        
    for tag in COMMON_HTML_TAGS:
        if page.find(tag):
            return True

    return False


def is_valid_date_format(date_string: str) -> tuple[bool, str]:
    date_formats = [
        DateForamt.DATE.value,
        DateForamt.T_DATE.value
    ]

    for format in date_formats:
        try:   
            datetime.strptime(date_string, format)
            return (True, format)
        except ValueError:
            return (False, None)

    return (False, None)