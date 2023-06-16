import sys
from app import Crawler
from util import timer
from db import GET
from classes import Provider


def main():
    PROVIDERS = GET.providers()
    cap = 10

    if len(sys.argv) > 1:
        cap = int(sys.argv[1])

    for provider in PROVIDERS:
        crawler = Crawler(provider[1], provider[2], provider[0])
        crawler.run(cap)


if __name__ == "__main__":
    timer(main)
