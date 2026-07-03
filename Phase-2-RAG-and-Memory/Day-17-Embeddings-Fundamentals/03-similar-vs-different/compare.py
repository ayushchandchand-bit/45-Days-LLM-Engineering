"""
Day 17 - Step 3: Similar vs different -- ranking by MEANING, not keywords.

We embed a query and a few documents, then score each doc against the query
with cosine similarity (higher = more alike). The "automobile" sentence ranks
near the top for "motor vehicle" even though they share NO words -- proof that
embeddings match meaning, not letters.

Setup: pip install sentence-transformers numpy
Run:   python compare.py
"""

from sentence_transformers import SentenceTransformer, util

DOCS = [
    "A car is a four-wheeled vehicle for the road",
    "An automobile takes you from place to place",     # 'car' meaning, different words
    "The chef cooked a delicious pasta dinner",
    "Photosynthesis lets plants make food from light",
]

QUERY = "How does a motor vehicle work?"


def main():
    print("Loading model (first run downloads ~90 MB)...\n")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Embed the query and all docs.
    query_vec = model.encode(QUERY)
    doc_vecs = model.encode(DOCS)

    # cos_sim returns a 1 x len(DOCS) matrix; [0] grabs the single row of scores.
    scores = util.cos_sim(query_vec, doc_vecs)[0]

    print(f"Query: {QUERY!r}\n")
    print("Documents ranked by meaning (higher = more similar):\n")

    # Pair each doc with its score and sort best-first.
    ranked = sorted(zip(DOCS, scores), key=lambda pair: float(pair[1]), reverse=True)
    for doc, score in ranked:
        print(f"  {float(score):+.3f}  {doc}")

    best = ranked[0][0]
    print(f"\nBest match: {best!r}")
    print("Notice 'automobile' scored high with ZERO shared words -- that's semantic search.")


if __name__ == "__main__":
    main()
