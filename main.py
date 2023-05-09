from app import Crawler
from util import timer


def main():
    c = Crawler("https://edition.cnn.com/business", "edition.cnn.com", "cnn")
    c.run()


if __name__ == "__main__":
    timer(main)
