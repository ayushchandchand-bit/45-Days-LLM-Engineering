"""
Day 17 - Exercise 1 (STUB): Semantic search over notes.

Given a query, return the most similar note by MEANING. Fill in the TODOs.

Setup: pip install sentence-transformers numpy
Run:   python semantic_search.py
"""

import numpy as np
from sentence_transformers import SentenceTransformer

NOTES = [
    "Buy milk and eggs from the market",
    "A bicycle or scooter is a cheap way to commute",
    "Finish the data structures assignment by Friday",
    "Recipe: boil rice, add dal and spices",
    "Book train tickets for the Diwali trip home",
]

QUERY = "something to ride to college"


def cosine(a, b):
    """Cosine similarity of two vectors. Higher = more alike."""
    # TODO: return the dot product of a and b divided by (norm(a) * norm(b)).
    #       Hint: np.dot(a, b) and np.linalg.norm(...)
    raise NotImplementedError


def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # TODO 1: embed the QUERY -> query_vec
    # TODO 2: embed all NOTES -> note_vecs (pass the whole list to model.encode)

    # TODO 3: build a list of (note, score) using cosine(query_vec, note_vec)
    #         for each note and its vector. (zip NOTES with note_vecs)

    # TODO 4: sort that list by score, highest first.

    # TODO 5: print each note with its score, then print the best match.
    raise NotImplementedError


if __name__ == "__main__":
    main()
