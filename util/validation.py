import re


def is_valid_link(link: str, key: str) -> bool:
    return key.lower() in link.lower()


def is_mail_link(link: str) -> bool:
    return link.startswith("mailto")


def is_sliced_link(link: str) -> bool:
    return link.startswith("/")


def is_html(link: str) -> bool:
    return link.endswith(".html") or link.endswith(".htm")


def is_id_string(link: str) -> bool:
    pattern = r"\b(?!-)(?:[a-f\d]+-){2,}[a-f\d]+(?!-)\b"
    return bool(re.search(pattern, link))


def is_paywall(page: str) -> bool:
    pattern = re.compile(r"^/signup.*", re.IGNORECASE)
    tags = page.find_all("a", href=pattern)
    print(tags)
    if tags:
        return True
    return False


def is_missing_title(page: str) -> bool:
    title = page.find("meta", property="og:title")
    if title:
        return False
    return True


def is_article(visited: set, link: str, provider: str, page: str) -> bool:
    if link in visited:
        return False

    if not is_valid_link(link, provider):
        return False

    if not is_html(link) and not is_id_string(link):
        return False

    if is_missing_title(page):
        return False

    common_html_tags = ["article", "section", "div"]

    for tag in common_html_tags:
        if page.find(tag):
            return True

    return False
