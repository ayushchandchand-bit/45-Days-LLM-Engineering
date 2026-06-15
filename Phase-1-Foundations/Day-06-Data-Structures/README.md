# Day 06 — Data Structures

A single variable holds one thing. Real programs juggle *collections*: a cart of items, a user's
profile fields, the unique tags on a post, a row of coordinates. Today you learn Python's four core
containers — **lists, dictionaries, tuples, sets** — what each is for, and how to pick the right one.
This is the most-used day of the whole Python week: every API response you'll parse in Phase 1 is
some nesting of lists and dicts (that's literally what JSON is).

> 🐙 **GitHub mini-track finale (Part 3 of 3).** Today's deck — *Branching & Collaboration: branches,
> merges, pull requests* (with an SVG branch-and-merge graph) — lives in
> [`github-basics/`](github-basics/). Open `github-basics/index.html`. Parts 1–2 were Days 4–5.

## Learning objectives
By the end of today you can:
- Build and mutate **lists**: index, slice, `append`/`insert`/`pop`/`remove`, `sort`/`reverse`
- Iterate lists with the Day-4 patterns, handle **nested lists**, and avoid the **copy-vs-reference** trap
- Use **dictionaries** (`key: value`): access, `.get()` with a default, add/update, `in`, delete
- Iterate dicts with **`.keys()` / `.values()` / `.items()`** and **merge** them
- Use **tuples** (immutable) and explain *why* immutability is useful (unpacking, keys, safety)
- Use **sets** for uniqueness and **set algebra** (`|` union, `&` intersection, `-` difference)
- **Choose the right structure** for a problem — the skill interviewers actually probe

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [lists](01-lists/) | create, index, slice, mutate (`append`/`insert`/`pop`/`remove`), membership |
| 02 | [list-patterns-and-nested](02-list-patterns-and-nested/) | iterate, `sort`/`reverse`, comprehensions, nested lists, copy vs reference |
| 03 | [dictionaries](03-dictionaries/) | `key: value`, access, `.get()`, add/update, `in`, `pop`/`del` |
| 04 | [dict-iteration-and-merging](04-dict-iteration-and-merging/) | `keys`/`values`/`items`, looping, merging, list-of-dicts |
| 05 | [tuples](05-tuples/) | immutability, unpacking, returning multiple values, when to use |
| 06 | [sets](06-sets/) | uniqueness, `add`, `in`, union/intersection/difference, when to use |
| 07 | [choosing-the-right-structure](07-choosing-the-right-structure/) | the comparison table + real scenarios |

Then test yourself in **[exercises/](exercises/)**.

## The 5 things to really nail today
1. **List = ordered & changeable; Tuple = ordered & fixed; Set = unique & unordered; Dict = labelled
   pairs.** Memorise this one-liner.
2. **`[]` is index/lookup, `{}` builds dicts/sets.** `d["key"]` reads a dict; `["a","b"][0]` reads a list.
3. **`.get(key, default)` never crashes**; `d[key]` raises `KeyError` if the key is missing.
4. **Lists are references.** `b = a` makes `b` point at the *same* list — change one, change both. Use
   `a.copy()` (or `a[:]`) for an independent copy.
5. **Sets kill duplicates instantly** and answer "what's common / what's different" with `&` and `-`.

## How to run
From this folder, run any file directly:

```bash
python 01-lists/lists.py
```

The Todo List exercise uses `input()` and will pause for you. Or experiment in the REPL:

```bash
python
>>> {"a": 1, "b": 2}.get("c", 0)
0
```

## Today's exercises
Three of them — see [`exercises/`](exercises/):
1. **Todo List Manager** — list `append`/`remove`/iterate behind a `while` menu (Day 4 + Day 6)
2. **Word Frequency Counter** — the classic dict + `.get()` text-analysis task
3. **Common Skills Finder** — set `&` / `|` / `-` to compare two candidates' skills

➡ Next: **[Day 07 — Errors, Modules & OOP](../Day-07-Errors-Modules-and-OOP/)**
