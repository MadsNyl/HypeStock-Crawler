from dataclasses import dataclass


@dataclass
class Provider:
    provider: str
    start_url: str
    base_url: str
