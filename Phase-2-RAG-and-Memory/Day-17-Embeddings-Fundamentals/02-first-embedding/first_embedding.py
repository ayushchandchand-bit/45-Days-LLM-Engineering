"""
Day 17 - Step 2: Your first REAL embedding (local, free, no API key).

We load a small trained model (all-MiniLM-L6-v2) and turn text into a vector
of 384 numbers. Unlike module 01, we don't pick the numbers -- the model does,
from having read billions of sentences.

First run downloads the model (~90 MB) to a local cache, then it's offline.

Setup: pip install sentence-transformers numpy
Run:   python first_embedding.py
"""

from sentence_transformers import SentenceTransformer


def main():
    print("Loading model 'all-MiniLM-L6-v2' (first run downloads ~90 MB)...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # --- one sentence -> one vector ---
    sentence = "I love learning about AI"
    vector = model.encode(sentence)

    print(f"\nText: {sentence!r}")
    print(f"Type:  {type(vector).__name__}")          # numpy.ndarray
    print(f"Shape: {vector.shape}")                    # (384,)  -> 384 numbers
    print(f"Dtype: {vector.dtype}")                    # float32

    # Show just the first 8 numbers so the output stays readable.
    preview = ", ".join(f"{x:+.3f}" for x in vector[:8])
    print(f"First 8 numbers: [{preview}, ...]")

    # This model returns unit-length vectors -- the "length" is ~1.0.
    length = float((vector ** 2).sum() ** 0.5)
    print(f"Vector length (norm): {length:.3f}   (~1.0 -> already normalized)")

    # --- many sentences at once -> one vector each ---
    sentences = [
        "The cat sat on the mat",
        "A feline rested on the rug",
        "Interest rates rose this quarter",
    ]
    vectors = model.encode(sentences)
    print(f"\nEncoded {len(sentences)} sentences at once -> shape {vectors.shape}")
    print("(rows = sentences, columns = the 384 features)")
    print("\nThe numbers look like noise to us -- but module 03 shows that")
    print("similar sentences get similar rows. That's the whole point.")


if __name__ == "__main__":
    main()
