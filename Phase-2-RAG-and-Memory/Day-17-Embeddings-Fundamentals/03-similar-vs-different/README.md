# 03 — Similar vs Different (Meaning, Not Keywords)

This is the payoff. We embed a handful of sentences, then ask: *which is closest in meaning to my
query?* The model will rank **"automobile"** near **"car"** even though they share **zero letters** —
something keyword search can never do.

## The setup
We have a few short "documents":

```python
docs = [
    "A car is a four-wheeled vehicle for the road",
    "An automobile takes you from place to place",   # same meaning as 'car', different words
    "The chef cooked a delicious pasta dinner",
    "Photosynthesis lets plants make food from light",
]
query = "How does a motor vehicle work?"
```

We embed the query **and** every doc, then score each doc against the query with **cosine
similarity** (a number from -1 to 1; **higher = more alike** — full formula in module 04). Here we
let the library compute it for us:

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")
doc_vecs   = model.encode(docs)
query_vec  = model.encode(query)
scores = util.cos_sim(query_vec, doc_vecs)[0]    # one score per doc
```

## What you'll see
The two vehicle sentences score **highest** against "How does a motor vehicle work?" — including the
"automobile" one with no shared words — while the pasta and photosynthesis sentences score low.

| Query | Top match | Why |
|-------|-----------|-----|
| "How does a motor vehicle work?" | the car / automobile sentences | same *meaning*, regardless of wording |

**That's semantic search.** Keyword search matches *letters*; embeddings match *meaning*. This single
behaviour is what makes RAG (next week) possible: store doc vectors, embed the question, return the
nearest docs.

## Gotcha: similarity is relative
Cosine scores aren't a percentage of "correctness". A score of 0.45 might be the best match in one
set and a poor one in another. You compare scores **within the same set** to find the *most* similar —
you don't read a single score as an absolute grade.

Run it:
```bash
python compare.py
```

➡ Next: [04-cosine-similarity](../04-cosine-similarity/) — compute that score yourself, with numpy.
