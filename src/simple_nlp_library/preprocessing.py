from typing import List


def lower_letters(text: str) -> str:
    text = text.replace("-", " ")
    return "".join([c.lower() for c in text if c.isalpha() or c.isspace() or c == "@"])


def single_spaces(text: str) -> str:
    return " ".join(text.split())


def non_stopword_tokens(tokens: List[str]) -> List[str]:
    stop_words = [
        "i",
        "me",
        "my",
        "myself",
        "we",
        "our",
        "ours",
        "ourselves",
        "you",
        "youre",
        "youve",
        "youll",
        "youd",
        "your",
        "yours",
        "yourself",
        "yourselves",
        "he",
        "him",
        "his",
        "himself",
        "she",
        "shes",
        "her",
        "hers",
        "herself",
        "it",
        "its",
        "its",
        "itself",
        "they",
        "them",
        "their",
        "theirs",
        "themselves",
        "what",
        "which",
        "who",
        "whom",
        "this",
        "that",
        "thatll",
        "these",
        "those",
        "am",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "having",
        "do",
        "does",
        "did",
        "doing",
        "a",
        "an",
        "the",
        "and",
        "but",
        "if",
        "or",
        "because",
        "as",
        "until",
        "while",
        "of",
        "at",
        "by",
        "for",
        "with",
        "about",
        "against",
        "between",
        "into",
        "through",
        "during",
        "before",
        "after",
        "above",
        "below",
        "to",
        "from",
        "up",
        "down",
        "in",
        "out",
        "on",
        "off",
        "over",
        "under",
        "again",
        "further",
        "then",
        "once",
        "here",
        "there",
        "when",
        "where",
        "why",
        "how",
        "all",
        "any",
        "both",
        "each",
        "few",
        "more",
        "most",
        "other",
        "some",
        "such",
        "no",
        "nor",
        "not",
        "only",
        "own",
        "same",
        "so",
        "than",
        "too",
        "very",
        "s",
        "t",
        "can",
        "will",
        "just",
        "don",
        "dont",
        "should",
        "shouldve",
        "now",
        "d",
        "ll",
        "m",
        "o",
        "re",
        "ve",
        "y",
        "ain",
        "aren",
        "arent",
        "couldn",
        "couldnt",
        "didn",
        "didnt",
        "doesn",
        "doesnt",
        "hadn",
        "hadnt",
        "hasn",
        "hasnt",
        "haven",
        "havent",
        "isn",
        "isnt",
        "ma",
        "mightn",
        "mightnt",
        "mustn",
        "mustnt",
        "needn",
        "neednt",
        "shan",
        "shant",
        "shouldn",
        "shouldnt",
        "wasn",
        "wasnt",
        "weren",
        "werent",
        "won",
        "wont",
        "wouldn",
        "wouldnt",
    ]
    return [token for token in tokens if token not in dict.fromkeys(stop_words)]


def non_social(tokens: List[str]) -> List[str]:
    return [token for token in tokens if not "@" in token and not token.startswith("http")]


def semantic_tokens(text: str) -> List[str]:
    text = lower_letters(text)
    text = single_spaces(text)
    tokens = non_social(non_stopword_tokens(text.split()))
    return tokens
