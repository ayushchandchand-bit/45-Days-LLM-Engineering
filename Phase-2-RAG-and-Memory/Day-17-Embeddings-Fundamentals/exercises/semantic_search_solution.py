"""
Day 17 - Exercise 1 (SOLUTION): Semantic search over notes.

Embed the query and every note, score with cosine similarity, rank best-first.
The 'bicycle or scooter' note wins for "something to ride to college" even
though those words never appear in it -- meaning beats keywords.

Setup: pip install sentence-transformers numpy
Run:   python semantic_search_solution.py
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
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def main():
    print("Loading model (first run downloads ~90 MB)...\n")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    query_vec = model.encode(QUERY)
    note_vecs = model.encode(NOTES)

    # Score every note against the query.
    scored = [(note, cosine(query_vec, vec)) for note, vec in zip(NOTES, note_vecs)]
    scored.sort(key=lambda pair: pair[1], reverse=True)   # best first

    print(f"Query: {QUERY!r}\n")
    print("Notes ranked by meaning (higher = more similar):\n")
    for note, score in scored:
        print(f"  {score:+.3f}  {note}")

    print(f"\nBest match: {scored[0][0]!r}")


if __name__ == "__main__":
    main()
