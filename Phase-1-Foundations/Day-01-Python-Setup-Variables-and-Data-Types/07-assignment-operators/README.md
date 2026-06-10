# 07 — Assignment Operators

You already know `=`. The **compound assignment operators** are shortcuts for "update a variable
using its own current value."

```python
score = 10
score = score + 5   # the long way
score += 5          # the short way — does the exact same thing
```

## The full set
| Operator | Means | Example | After (start = 10) |
|:--------:|-------|---------|:------------------:|
| `+=` | add & store | `x += 3` | `13` |
| `-=` | subtract & store | `x -= 3` | `7` |
| `*=` | multiply & store | `x *= 3` | `30` |
| `/=` | divide & store (→ float) | `x /= 4` | `2.5` |
| `//=` | floor-divide & store | `x //= 3` | `3` |
| `%=` | modulo & store | `x %= 3` | `1` |
| `**=` | power & store | `x **= 2` | `100` |

## Why they matter
Counting and accumulating are everywhere — running totals, loop counters, scores. `+=` is the
idiom you'll type thousands of times:

```python
total = 0
total += 199    # item 1
total += 49     # item 2
# total is now 248
```

> These also work on strings and lists later: `name += "!"`, `cart += [item]`.

Run the example:

```bash
python assignment_operators.py
```

➡ Next: [08-print-function](../08-print-function/)
