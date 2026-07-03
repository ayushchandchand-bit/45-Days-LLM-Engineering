# Day 17 — Exercises

Practise turning text into vectors and comparing them. Both exercises use the **local** model
(`all-MiniLM-L6-v2`) and the **cosine similarity** you wrote in module 04 — no API key needed.

Fill in the `# TODO`s in each stub, then check against the `_solution.py`.

```bash
pip install -r requirements.txt        # numpy, sentence-transformers
```

## 1. Semantic search — `semantic_search.py`
You have a small list of "notes". Given a **query**, return the **single most similar note** by
meaning (not keywords).

- Embed the query and all notes with `model.encode(...)`.
- Score each note against the query with cosine similarity.
- Print the notes ranked best-first, and the top match.

**Try this:** query `"something to ride to college"` should surface the *bicycle / scooter* note,
even though those exact words aren't in your query. That's the win — meaning over keywords.

➡ Solution: [`semantic_search_solution.py`](semantic_search_solution.py)

## 2. Odd one out — `odd_one_out.py`
Given a list of words, find the **one that fits least** with the rest (e.g.
`["apple", "banana", "mango", "rocket"]` → `rocket`).

- Embed every word.
- For each word, compute its **average** cosine similarity to all the *other* words.
- The word with the **lowest** average is the odd one out.

This is your first taste of using embeddings to find an **outlier** — handy for cleaning data later.

➡ Solution: [`odd_one_out_solution.py`](odd_one_out_solution.py)

➡ Back to [Day 17](../README.md).
