"""
Day 17 - Exercise 2 (STUB): Find the odd one out.

Given a list of words, find the one that fits LEAST with the rest, e.g.
["apple", "banana", "mango", "rocket"] -> "rocket".

Idea: for each word, average its cosine similarity to all the OTHER words.
The word with the lowest average is the outlier. Fill in the TODOs.

Setup: pip install sentence-transformers numpy
Run:   python odd_one_out.py
"""

import numpy as np
from sentence_transformers import SentenceTransformer

WORDS = ["apple", "banana", "mango", "grapes", "rocket"]


def cosine(a, b):
    """Cosine similarity of two vectors."""
    # TODO: return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)) as a float
    raise NotImplementedError


def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # TODO 1: embed all WORDS -> vectors

    # TODO 2: for each word i, compute the AVERAGE cosine similarity to every
    #         OTHER word j (skip j == i). Store (word, avg_similarity).

    # TODO 3: the odd one out is the word with the LOWEST average similarity.
    #         Print each word's average, then announce the outlier.
    raise NotImplementedError


if __name__ == "__main__":
    main()
