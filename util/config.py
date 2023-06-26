from db import GET
from .http import http_get


def load_config_settings() -> dict | None:
    config_url = GET.config_url()

    if not config_url:
        return

    try:
        res = http_get(config_url)
        return res.json()
    except Exception as e:
        return