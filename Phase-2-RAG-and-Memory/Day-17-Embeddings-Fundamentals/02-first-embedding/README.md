# 02 — Your First Real Embedding

In module 01 *we* hand-picked 2 numbers per word. Now a **trained model** picks the numbers for us —
hundreds of them — from the actual text. No API key, no internet (after the first download): it runs
on your laptop.

## The model: `all-MiniLM-L6-v2`
A small, fast, free embedding model from the `sentence-transformers` library. It turns **any
sentence** into a vector of **384 numbers**. "MiniLM" = a mini language model; "384" is just how many
features it was designed to output.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")     # first run downloads ~90 MB, then cached
vector = model.encode("I love learning about AI")   # -> a numpy array of 384 floats
```

> **First run is slow** — it downloads the model once to a local cache. Every run after that loads
> from disk in a second or two.

## What you get back
`model.encode(text)` returns a **numpy array** — a row of 384 floating-point numbers like
`[ 0.043, -0.011, 0.067, ... ]`. That row *is* the embedding. Key things to notice in the output:

| Property | Value | Means |
|----------|-------|-------|
| `vector.shape` | `(384,)` | 384 numbers — the model's "features" |
| `vector.dtype` | `float32` | each feature is a decimal |
| length / norm | ~`1.0` | this model returns **unit-length** vectors (handy for module 04) |

You won't be able to *read meaning* in the 384 numbers — they're not human-labelled like our
"animal-ness" axis was. That's fine. The model only promises one thing: **similar sentences get
similar rows**. We prove that in module 03.

## Encoding many at once
You can pass a **list** of texts and get a vector for each — far faster than one call per text:

```python
vectors = model.encode(["first sentence", "second sentence"])
print(vectors.shape)        # (2, 384)  -> 2 rows, 384 columns
```

This batch form is what real apps use (embed a whole folder of notes in one call).

Run it (downloads the model on first run):
```bash
python first_embedding.py
```

➡ Next: [03-similar-vs-different](../03-similar-vs-different/) — see similar meaning ⇒ similar vectors.
