from enum import Enum


class Pattern(Enum):
    ID_STRING = r"\b(?!-)(?:[a-f\d]+-){2,}[a-f\d]+(?!-)\b"
    HYPHEN_STRING = r"\w+-\w+"
    SIGNUP = r"^/signup.*"