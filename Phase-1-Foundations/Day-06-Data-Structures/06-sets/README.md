# 06 — Sets

A **set** is an **unordered collection of unique items**. Two superpowers: it **kills duplicates**
automatically, and it does **set algebra** (what's common, what's combined, what's different) in one
character.

```python
tags = {"python", "ai", "python", "ml"}   # curly braces, no key:value
print(tags)                                # {'python', 'ai', 'ml'} — dupes gone
"ai" in tags                               # True — membership is very fast
tags.add("rag")                            # add one
tags.discard("ml")                         # remove (no error if absent)
```
⚠️ `{}` alone is an **empty dict**, not a set. For an empty set use `set()`.

## Deduplicate instantly
```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
unique = set(emails)            # {'a@x.com', 'b@x.com'}
len(set(emails))                # count distinct
list(set(emails))               # back to a list if you need order/indexing
```

## Set algebra (the reason sets exist)
```python
a = {"python", "sql", "git"}
b = {"python", "excel"}
a & b      # {'python'}                  intersection — in BOTH
a | b      # {'python','sql','git','excel'}   union — in EITHER
a - b      # {'sql', 'git'}             difference — in a but NOT b
a ^ b      # {'sql','git','excel'}      symmetric diff — in exactly one
```

## When to use a set
- You need **uniqueness** (tags, visited-IDs, distinct values).
- You ask **"is X in here?"** a lot (membership tests are faster than in a list).
- You need **common / combined / different** between two groups.
- ❌ Not when order matters or you need duplicates/indexing — use a list.

## 🎤 Talking points (what to say & focus on)
- **Two jobs: dedupe + compare.** Lead with `set(my_list)` deleting duplicates in one move — instantly
  useful. Then set algebra for comparing groups.
- **`&`, `|`, `-` map to plain English:** AND (common), OR (combined), MINUS (only-in-the-first). The
  "skills in common between two candidates" example sells it — it's the exercise, too.
- **`{}` is a dict, not a set!** The empty-set gotcha bites everyone. `set()` for empty. Say it twice.
- **Unordered + no duplicates + no indexing.** You can't do `s[0]`. If you catch yourself wanting an
  index or duplicates, you wanted a list. Frame the trade-off clearly.
- **Fast membership is the quiet superpower** — `x in big_set` vs `x in big_list`. Mention it for when
  they're checking membership in a loop over lots of data (dedup IDs, seen-URLs in a crawler).

## ⚠️ Common mistakes to call out
- `{}` creates an empty **dict**, not a set. Use `set()`.
- Expecting sets to keep order or support `s[0]` indexing — they do neither.
- Trying to add a list to a set → `TypeError` (members must be immutable; use a tuple).
- Using `.remove(x)` on an absent item → `KeyError`; use `.discard(x)` to be safe.

Run the examples:

```bash
python sets.py
```

➡ Next: **[07-choosing-the-right-structure](../07-choosing-the-right-structure/)**
