# 05 — Tuples

A **tuple** is an **ordered but unchangeable** (immutable) collection. Think "a fixed record" — once
made, it can't be edited. You've already been using them: returning multiple values (Day 5) makes a
tuple, and `(name, price)` line items are tuples.

```python
point = (3, 4)                # round brackets (or even just: 3, 4)
point[0]                      # 3   (index like a list)
len(point)                    # 2
# point[0] = 9                # ❌ TypeError — tuples can't be changed
x, y = point                  # unpack into two variables
```

## List vs tuple — when to use which
| | List `[]` | Tuple `()` |
|--|-----------|------------|
| Changeable? | Yes (mutable) | **No** (immutable) |
| Use for | a collection that grows/shrinks | a fixed group that belongs together |
| Example | a shopping cart | a `(latitude, longitude)` coordinate |

## Why immutability is a *feature*
- **Safety** — a tuple can't be changed by accident; great for constants and config that shouldn't move.
- **Dict keys / set members** — only *immutable* things can be keys/members. `{(0,0): "start"}` works;
  a list key raises `TypeError`.
- **Intent** — using a tuple signals "these belong together and won't change" (an RGB colour, a
  database row, a coordinate).

## Unpacking — the everyday tuple superpower
```python
person = ("Asha", 21, "Pune")
name, age, city = person          # one line, three variables
a, b = b, a                       # swap without a temp variable!
for name, marks in [("Asha", 88), ("Ben", 72)]:   # unpack each tuple
    ...
```

## 🎤 Talking points (what to say & focus on)
- **"A tuple is a list that's been frozen."** Same indexing/slicing/iteration; the difference is you
  *can't change it*. Demo the `TypeError` on item assignment so the wall is real.
- **They've already used tuples** — Day-5 `return a, b` and the `(name, price)` items. Reveal that;
  it makes tuples feel familiar, not new.
- **Immutability is the *why*.** Three concrete payoffs: safety (can't be clobbered), usable as dict
  keys / set members, and signalling intent. The `{(lat, lon): name}` example is the killer — lists
  can't do that.
- **Unpacking is the daily win.** `name, age, city = person` and the no-temp swap `a, b = b, a`.
  Then tie to looping list-of-tuples. This is idiomatic, clean Python they'll write forever.
- **Single-element tuple gotcha:** `(5)` is just `5`; you need the trailing comma `(5,)`. Quick but
  worth showing — it confuses people.

## ⚠️ Common mistakes to call out
- Trying to change a tuple item → `TypeError`.
- `(5)` is an int, not a tuple — a one-item tuple needs the comma: `(5,)`.
- Unpacking with the wrong number of names → `ValueError: too many/not enough values`.
- Reaching for a tuple when the data genuinely needs to change (use a list).

Run the examples:

```bash
python tuples.py
```

➡ Next: **[06-sets](../06-sets/)**
