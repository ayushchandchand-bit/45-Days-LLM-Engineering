# 01 — What Is an Embedding? (Meaning as Coordinates)

Before we touch a single library, let's get the idea in your bones with numbers you can read.

## The core idea
An **embedding** is a list of numbers (a **vector**) that represents a piece of text. The trick is
*how* the numbers are chosen: a good embedding model places texts so that **similar meanings get
similar numbers**.

Think of a map. A city is just two numbers — (latitude, longitude). Cities that are *near* on the
map have *near* coordinates. Embeddings do the same thing for **meaning** instead of geography —
except instead of 2 numbers they usually use hundreds.

## A tiny hand-made example
Imagine we describe words with just **2 made-up features**:

- axis 1 → "how *animal* is it?"
- axis 2 → "how *vehicle* is it?"

| Word | animal | vehicle | As a point |
|------|:------:|:-------:|------------|
| `cat`   | 0.9 | 0.1 | (0.9, 0.1) |
| `dog`   | 0.8 | 0.2 | (0.8, 0.2) |
| `car`   | 0.1 | 0.9 | (0.1, 0.9) |
| `truck` | 0.2 | 0.8 | (0.2, 0.8) |

Plot those and `cat`/`dog` huddle in one corner, `car`/`truck` in another. **Closeness on the map =
closeness in meaning.** `cat` is near `dog`; both are far from `car`.

```
vehicle
  1.0 |        car  truck
      |
      |
  0.0 |  cat dog
      +-------------------- animal
       0.0              1.0
```

## How "close" do we measure?
The simplest measure is **straight-line (Euclidean) distance** — the same `sqrt((x2-x1)^2 + ...)`
you've seen in maths. Smaller distance = more alike. `coordinates.py` computes it by hand for the
table above, with **no libraries**, so you can see there's no magic.

> Tomorrow's modules use **cosine similarity** instead of distance (it cares about *direction*, not
> *length*) — but the intuition is identical: one number that says how alike two vectors are.

## The catch (why we need a model)
Nobody hand-assigns these numbers. Real text has far more than 2 features — is it formal? past
tense? about money? A real embedding model learned from billions of sentences picks **hundreds** of
features for you. We hand-pick 2 here only to *see* the idea. From module 02 on, a model does it.

Run it (no install needed — pure Python):
```bash
python coordinates.py
```

➡ Next: [02-first-embedding](../02-first-embedding/) — let a real model turn text into 384 numbers.
