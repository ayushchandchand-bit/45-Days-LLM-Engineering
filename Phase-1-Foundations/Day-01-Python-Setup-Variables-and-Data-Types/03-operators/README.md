# 03 — Operators

Operators let you *do things* with numbers.

## Arithmetic operators
| Operator | Name | Example | Result |
|:--------:|------|---------|:------:|
| `+` | add | `3 + 2` | `5` |
| `-` | subtract | `3 - 2` | `1` |
| `*` | multiply | `3 * 2` | `6` |
| `/` | divide (always float) | `7 / 2` | `3.5` |
| `//` | **floor** divide (drops remainder) | `7 // 2` | `3` |
| `%` | **modulo** (the remainder) | `7 % 2` | `1` |
| `**` | exponent (power) | `3 ** 2` | `9` |

## The two you'll forget — but shouldn't
- `//` **floor division**: divides and rounds *down* to a whole number. `17 // 5` → `3`.
- `%` **modulo**: gives the *remainder*. `17 % 5` → `2`. Hugely useful for "is this even?"
  (`n % 2 == 0`) and "every Nth item" logic.

## Operator precedence (order of operations)
Python follows math: `**` first, then `*  /  //  %`, then `+  -`. Use parentheses when in doubt.

```python
>>> 2 + 3 * 4        # 14, not 20 — multiplication first
>>> (2 + 3) * 4      # 20 — parentheses force the order
```

Run the examples:

```bash
python operators.py
```

➡ Next: [04-comments](../04-comments/)
