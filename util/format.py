from datetime import datetime
from .validation import is_valid_date_format


def string_to_datetime(date_string: str) -> datetime:
    date_string = date_string[:19]
    is_valid, format = is_valid_date_format(date_string)
    if is_valid:
        return datetime.strptime(date_string, format)
    
    return None


def build_link(base_url: str, link: str) -> str:
    return f"https://{base_url}{link}"
