from datetime import datetime


def string_to_datetime(date_string: str) -> datetime:
    date_string = date_string[:19]
    return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
