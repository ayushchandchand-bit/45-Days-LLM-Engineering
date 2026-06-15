# 07 — Choosing the Right Structure

You now know all four containers. The real skill — and a favourite interview probe — is picking the
right one. This module is the decision guide.

## The cheat sheet
| Structure | Syntax | Ordered? | Changeable? | Duplicates? | Reach for it when… |
|-----------|--------|:--------:|:-----------:|:-----------:|--------------------|
| **List** | `[1, 2, 3]` | ✅ yes | ✅ yes | ✅ yes | a sequence that grows/shrinks; order matters |
| **Tuple** | `(1, 2, 3)` | ✅ yes | ❌ no | ✅ yes | a fixed record; dict keys; "won't change" |
| **Set** | `{1, 2, 3}` | ❌ no | ✅ yes | ❌ no | uniqueness; fast membership; compare groups |
| **Dict** | `{"a": 1}` | ✅ (insertion) | ✅ yes | keys unique | look up a value **by name/key** |

## Ask yourself, in order
1. **Do I look things up by a name/label?** → **dict**.
2. **Do I need only unique items, or to compare groups?** → **set**.
3. **Must it never change (or be a dict key)?** → **tuple**.
4. **Otherwise** (an ordered, editable sequence) → **list**.

## Real scenarios
| Problem | Best fit | Why |
|---------|----------|-----|
| A shopping cart | list | ordered, items added/removed, dups allowed |
| A user profile (name, age, email) | dict | look up fields by name |
| RGB colour `(255, 0, 0)` | tuple | fixed 3 values, used as a key/constant |
| Unique tags on a blog post | set | no duplicate tags |
| Word → count tally | dict | look up a count by the word |
| `(latitude, longitude)` | tuple | fixed pair, can be a dict key |
| Distinct visitor IDs today | set | uniqueness + fast "seen it?" |
| Rows of a CSV | list **of dicts** | ordered rows, each a named record |

## They nest — that's the real world
The structures combine, and that nesting *is* JSON / API data:
```python
classroom = {                          # dict
    "subject": "AI",
    "students": [                      # list
        {"name": "Asha", "tags": {"python", "ml"}},   # dict with a set
        {"name": "Ben",  "tags": {"sql"}},
    ],
}
```

## 🎤 Talking points (what to say & focus on)
- **This module is judgment, not syntax.** Put the cheat sheet on screen and run the 4-question
  decision flow against each real scenario *out loud*. The repetition builds the instinct.
- **Do it as a quiz.** Read a scenario ("track which coupon codes were already used"), let them shout
  the structure + the *why*. Right answer matters less than the reasoning.
- **The nesting example is the punchline.** Show the `classroom` dict and name each layer. Then say:
  "this is a JSON response — in Phase 1 you'll `response['students'][0]['name']` all day." It makes
  the whole day's payoff concrete.
- **Performance footnote (don't overdo):** "x in set" beats "x in list" for big collections; dict/set
  lookups are near-instant. Enough for them to choose a set for membership-heavy loops.
- **There's rarely one "right" answer** — but there's usually a clearly *wrong* one (a list where you
  needed unique lookup). Teach them to avoid the wrong one.

## ⚠️ Common mistakes to call out
- Using a list and writing slow `x in big_list` checks where a set belongs.
- Using parallel lists (`names[i]`, `ages[i]`) where a list of dicts is far cleaner.
- Reaching for a dict when a list is enough (no real "key" — just a sequence).
- Forgetting these nest — flattening data that's naturally hierarchical.

Run the examples:

```bash
python choosing.py
```

➡ Next: **[exercises/](../exercises/)** — Todo List, Word Frequency Counter & Common Skills Finder
