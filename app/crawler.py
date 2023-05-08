from .scraper import Scraper


class Crawler(Scraper):
    def run(self, url: str) -> None:
        self._crawl(url)

    def _crawl(self, url: str) -> None:
        page = super()._get_html(url)
        links = super()._get_links(page)
        # TODO: implement graph traversing for links
