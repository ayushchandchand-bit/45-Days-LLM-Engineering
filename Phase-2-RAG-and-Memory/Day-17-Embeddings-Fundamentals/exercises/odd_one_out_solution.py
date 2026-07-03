"""
Day 17 - Exercise 2 (SOLUTION): Find the odd one out.

For each word, average its cosine similarity to all the OTHER words.
The word with the lowest average sticks out -- here, 'rocket' among fruits.

Setup: pip install sentence-transformers numpy
Run:   python odd_one_out_solution.py
"""

import numpy as np
from sentence_transformers import SentenceTransformer

WORDS = ["apple", "banana", "mango", "grapes", "rocket"]


def cosine(a, b):
    """Cosine similarity of two vectors."""
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def main():
    print("Loading model (first run downloads ~90 MB)...\n")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    vectors = model.encode(WORDS)

    # Average similarity of each word to all the others.
    averages = []
    for i, word in enumerate(WORDS):
        sims = [cosine(vectors[i], vectors[j]) for j in range(len(WORDS)) if j != i]
        averages.append((word, sum(sims) / len(sims)))

    print("Average similarity of each word to the rest (lower = more out of place):\n")
    for word, avg in sorted(averages, key=lambda pair: pair[1], reverse=True):
        print(f"  {avg:+.3f}  {word}")

    odd = min(averages, key=lambda pair: pair[1])[0]
    print(f"\nOdd one out: {odd!r}")


if __name__ == "__main__":
    main()
