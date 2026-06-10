# 02 — Numbers: Integers & Floats

Python has two everyday number types:

| Type | What it is | Examples |
|------|------------|----------|
| `int` | whole numbers (no decimal point) | `0`, `42`, `-7`, `1000000` |
| `float` | numbers with a decimal point | `3.14`, `-0.5`, `2.0` |

```python
>>> type(42)
<class 'int'>
>>> type(3.14)
<class 'float'>
```

## Key things to know
- **Any division (`/`) gives a float**, even `4 / 2` → `2.0`.
- Floats can be imprecise (`0.1 + 0.2` → `0.30000000000000004`). That's normal for *all*
  programming languages — it's how computers store decimals. Don't panic.
- Ints in Python can be **arbitrarily large** — no overflow. `2 ** 1000` just works.

## Numeric notations (nice-to-know)
```python
1_000_000     # underscores for readability → 1000000
0xFF          # hexadecimal → 255
0b1010        # binary → 10
1e3           # scientific notation → 1000.0 (a float)
```

Run the examples:

```bash
python numbers.py
```

➡ Next: [03-operators](../03-operators/)
