# 03 — Dictionaries

A **dictionary** stores data as **`key: value` pairs** — labelled, not numbered. When you think "look
this up *by name*" (a user by id, a price by product, a setting by its key), you want a dict. This is
*the* structure of the AI era: a JSON API response is a dict, an LLM's structured output is a dict.

```python
student = {                       # curly braces, key: value pairs
    "name": "Asha",
    "age": 21,
    "marks": [88, 72, 95],        # values can be anything (even lists!)
}
student["name"]                   # "Asha"   -> look up BY KEY (not position)
len(student)                      # 3 pairs
"age" in student                  # True     -> `in` checks the KEYS
```

## Access safely: `[]` vs `.get()`
```python
student["email"]                  # ❌ KeyError — key doesn't exist
student.get("email")              # None — safe, no crash
student.get("email", "n/a")       # "n/a" — your own default
```
Use `.get(key, default)` whenever a key *might* be missing — it's the safe, idiomatic lookup.

## Add / update / delete
```python
student["email"] = "asha@x.com"   # add a new pair (or update if key exists)
student["age"] = 22               # update existing
del student["age"]                # delete a pair  (KeyError if missing)
removed = student.pop("marks")    # delete & RETURN the value
```

## 🎤 Talking points (what to say & focus on)
- **"A dict is a real dictionary: look up a *word* (key), get its *definition* (value)."** Contrast
  with lists: lists answer "what's at position 2?", dicts answer "what's the value for 'name'?".
- **Keys are unique; values are anything.** Assigning an existing key overwrites. Values can be lists,
  even other dicts — that nesting *is* JSON. Show a value that's a list.
- **`.get()` is the single most useful dict habit.** `d[k]` crashes on a missing key; `.get(k, default)`
  doesn't. Demo the `KeyError`, then the graceful `.get`. They'll use this constantly parsing API data.
- **`in` checks keys, not values.** `"age" in student` → True; `21 in student` → False. Common
  surprise — call it out.
- **AI tie-in, hard:** "Every response from Groq/OpenAI is a nested dict. Today you're learning to
  read it." That framing makes the module feel essential, because it is.

## ⚠️ Common mistakes to call out
- `d["missing"]` → `KeyError`. Reach for `.get()` when unsure.
- Thinking `in` checks values (it checks keys).
- Using a list as a key → `TypeError` (keys must be immutable — strings, numbers, tuples).
- Expecting dict order to be "sorted" — it preserves *insertion* order, not sorted order.

Run the examples:

```bash
python dictionaries.py
```

➡ Next: **[04-dict-iteration-and-merging](../04-dict-iteration-and-merging/)**
