from dataclasses import dataclass
from datetime import datetime


@dataclass
class MetaData:
    title: str
    created_date: datetime
