import re


def is_valid_link(link: str, key: str) -> bool:
    return key.lower() in link.lower()


def is_sliced_link(link: str) -> bool:
    return link.startswith("/")


def is_html(link: str) -> bool:
    return link.endswith(".html") or link.endswith(".htm")


def is_id_string(link: str) -> bool:
    pattern = r"\b(?!-)(?:[a-f\d]+-){2,}[a-f\d]+(?!-)\b"
    return bool(re.search(pattern, link))
