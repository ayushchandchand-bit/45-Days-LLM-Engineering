"""
Day 17 - Step 4: Cosine similarity by hand (numpy).

We write the closeness formula ourselves:
    cosine(a, b) = (a . b) / (||a|| * ||b||)
...then run it on real embeddings and confirm it matches the library's
util.cos_sim. After this there is no black box left for tomorrow's
from-scratch semantic search.

Setup: pip install sentence-transformers numpy
Run:   python cosine.py
"""

import numpy as np
from sentence_transformers import SentenceTransformer, util


def cosine(a, b):
    """Angle-based similarity of two vectors. +1 = same, 0 = unrelated, -1 = opposite."""
    dot = np.dot(a, b)                                   # a1*b1 + a2*b2 + ...
    return dot / (np.linalg.norm(a) * np.linalg.norm(b))  # divide by both lengths


def main():
    print("Loading model (first run downloads ~90 MB)...\n")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    a = model.encode("A car is a fast road vehicle")
    b = model.encode("An automobile drives on the highway")   # similar meaning
    c = model.encode("I baked a chocolate cake today")        # unrelated

    # Our hand-written cosine.
    sim_ab = cosine(a, b)
    sim_ac = cosine(a, c)

    print("Our cosine():")
    print(f"  car  vs automobile : {sim_ab:+.3f}   (related   -> high)")
    print(f"  car  vs cake       : {sim_ac:+.3f}   (unrelated -> low)")

    # Cross-check against the library so you can trust our version.
    lib_ab = float(util.cos_sim(a, b)[0][0])
    print(f"\nLibrary util.cos_sim for car vs automobile: {lib_ab:+.3f}")
    print(f"Matches our value? {np.isclose(sim_ab, lib_ab)}")

    # Shortcut: this model returns unit-length vectors, so cosine == dot product.
    print(f"\n||a|| = {np.linalg.norm(a):.3f}  (~1.0 -> unit length)")
    print(f"Plain dot product a . b = {np.dot(a, b):+.3f}  (same as cosine above)")
    print("That's why vector DBs normalize once, then only need a fast dot product.")


if __name__ == "__main__":
    main()
