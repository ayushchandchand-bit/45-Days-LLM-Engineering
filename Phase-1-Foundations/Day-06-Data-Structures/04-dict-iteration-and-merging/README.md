# 04 — Dict Iteration & Merging

Once you can build a dict, you need to *walk* it and *combine* dicts. And the single most common
real-world shape — a **list of dicts** (rows of records) — comes together here.

## The three views
```python
prices = {"coffee": 120, "tea": 80}
prices.keys()      # dict_keys(['coffee', 'tea'])
prices.values()    # dict_values([120, 80])
prices.items()     # dict_items([('coffee', 120), ('tea', 80)])
```
Loop them:
```python
for key in prices:               # looping a dict gives its KEYS by default
    ...
for key, value in prices.items():   # the idiomatic way to get both
    print(key, value)
```

## Merging dicts
```python
defaults = {"theme": "light", "lang": "en"}
user     = {"lang": "hi"}
settings = {**defaults, **user}     # {'theme':'light', 'lang':'hi'} — user WINS
defaults.update(user)               # same effect, mutates `defaults` in place
```
Right-most wins on key clashes — exactly what you want for "defaults, then overrides."

## The killer combo: a list of dicts (records)
```python
students = [
    {"name": "Asha", "marks": 88},
    {"name": "Ben",  "marks": 72},
]
for s in students:                 # each s is a dict (one record/row)
    print(s["name"], s["marks"])
students.sort(key=lambda s: s["marks"], reverse=True)   # rank by a field
```
This is *the* structure of a CSV file, a database query result, and a JSON API list. Master this and
half of data work is muscle memory.

## 🎤 Talking points (what to say & focus on)
- **Looping a dict gives KEYS** by default; `.items()` gives key+value pairs. Show both; make
  `for k, v in d.items():` the reflex.
- **`.items()` unpacking mirrors Day-5 tuples** — `for k, v in ...` is tuple unpacking in disguise.
  Connect it; it's not new magic.
- **Merging with `{**a, **b}`: right wins.** Frame it as "defaults then user overrides" — the exact
  pattern for app config. Show `.update()` as the in-place twin.
- **List-of-dicts is the whole point of the module.** Spend the most time here. It's CSV rows, DB
  results, JSON arrays. Show looping, then `sort(key=lambda r: r["field"])`. This is the bridge to
  every real dataset they'll touch.
- **Build-a-dict-in-a-loop (count pattern):** previews the word-frequency exercise — `counts[word] =
  counts.get(word, 0) + 1`. Show it once; it's the most useful dict idiom there is.

## ⚠️ Common mistakes to call out
- Expecting `for x in dict` to give values (it gives keys).
- Modifying a dict's size while iterating over it → `RuntimeError`. Iterate a copy of the keys if you must.
- Forgetting `.items()` and writing `for k in d: v = d[k]` (works, but `.items()` is cleaner).
- Merging in the wrong order so the wrong dict "wins" on clashes.

Run the examples:

```bash
python dict_iteration.py
```

➡ Next: **[05-tuples](../05-tuples/)**
