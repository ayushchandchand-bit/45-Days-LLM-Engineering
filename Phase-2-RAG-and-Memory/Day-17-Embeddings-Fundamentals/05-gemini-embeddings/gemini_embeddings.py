"""
Day 17 - Step 5: Gemini cloud embeddings (OPTIONAL).

Same idea as the local model -- text in, vector out, cosine to compare --
but the vector comes from Google's hosted API instead of your laptop.
This is optional: it needs a free GEMINI_API_KEY. With no key, the script
prints a friendly note and exits, so the rest of Day 17 still runs.

Setup: pip install google-genai numpy python-dotenv   (+ GEMINI_API_KEY in .env)
Get a free key: https://aistudio.google.com/apikey
Run:   python gemini_embeddings.py
"""

import os

import numpy as np
from dotenv import load_dotenv

load_dotenv()

MODEL = "gemini-embedding-001"


def cosine(a, b):
    """Same closeness formula as module 04 -- works on any vectors."""
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("No GEMINI_API_KEY found -- this module is optional, skipping.")
        print("To try it: put GEMINI_API_KEY=... in a .env file (see the README).")
        print("The local model in modules 02-04 needs no key and is our default.")
        return

    # Imported here so the no-key message above works even without the package.
    from google import genai

    client = genai.Client(api_key=api_key)

    def embed(text):
        result = client.models.embed_content(model=MODEL, contents=text)
        return result.embeddings[0].values            # a list of floats

    a = embed("A car is a fast road vehicle")
    b = embed("An automobile drives on the highway")  # similar meaning
    c = embed("I baked a chocolate cake today")       # unrelated

    print(f"Gemini embedding size: {len(a)} numbers per vector\n")
    print("Cosine similarity (higher = more alike):")
    print(f"  car vs automobile : {cosine(a, b):+.3f}   (related   -> high)")
    print(f"  car vs cake       : {cosine(a, c):+.3f}   (unrelated -> low)")
    print("\nSame pattern as the local model -- the provider is swappable.")


if __name__ == "__main__":
    main()
